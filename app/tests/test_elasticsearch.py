from django.test import TestCase
from django.contrib.auth.models import User

from elasticsearch_dsl import Q

from ..documents import ProductInventoryDocument
from ..models import Products

import datetime

class TestSearch(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(
            username='Pujan', email='pujan@gmail.com', password='pujanpujan')
        Products.objects.create(
            user=self.user, title='laptop', description='acer nitro 5 | 1TB | GTX 3060 | 8GB Ram')    
        Products.objects.create(
            user=self.user, title='Mobile Phone', description='Redmi Note 7 Pro | 2017 Model')   
        Products.objects.create(
            user=self.user, title='new laptop', description='macbook | M1 chip | 2021 Model')     
        return super().setUp()
    
    def search_query(self, query):
        search_document = ProductInventoryDocument
        q = Q(
                'multi_match',
                query= query,
                type= "phrase_prefix",
                fields=['title', 'description'],
                )
        search = search_document.search().query(q)
        response = search.execute()
        return response

    def test_search(self):
        response = self.search_query(query='redmi')
        results = {r['title'] for r in response}
        assert results == {'Mobile Phone'}
        
