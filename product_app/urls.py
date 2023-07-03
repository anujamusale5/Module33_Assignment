from .views import ProductList,ProductListById
from django.urls import path

urlpatterns= [
   path('productdetail/',ProductList.as_view(),name='product-list'),
   path('productdetail/<int:id>/',ProductListById.as_view(),name='product-single')
]