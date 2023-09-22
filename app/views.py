from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from elasticsearch_dsl import Q

from django.http import HttpResponse
from .serializer import ProductSerializer
from .models import Products
from .documents import ProductInventoryDocument


@api_view(['GET'])
def home_page(request):
    product_query = Products.objects.all()
    serializer = ProductSerializer(product_query, many= True)
    return Response(serializer.data, status=status.HTTP_200_OK)

class SearchProductInventory(APIView, LimitOffsetPagination):
    productinventory_serializer = ProductSerializer
    search_document = ProductInventoryDocument

    def get(self, request, query):
        print('request', request)
        print('query', query)
        try:
            q = Q(
                'multi_match',
                query= query,
                type= "phrase_prefix",
                fields=['title', 'description'],
                )
            search = self.search_document.search().query(q)
            response = search.execute()

            results = self.paginate_queryset(response, request,view=self)
            serializer = self.productinventory_serializer(results, many=True)
            
            return self.get_paginated_response(serializer.data)
            
        except Exception as e:
            return HttpResponse(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

