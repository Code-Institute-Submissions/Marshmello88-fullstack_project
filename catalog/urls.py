from django.urls import path
from . import views


urlpatterns = [
    path('search/', views.search, name='search_results'), # trying out
    path('', views.all_products, name='products'),
]

