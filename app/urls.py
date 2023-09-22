from rest_framework.urlpatterns import format_suffix_patterns
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('search/<str:query>', views.SearchProductInventory.as_view(), name='search'),
]

urlpatterns = format_suffix_patterns(urlpatterns)