from django.urls import path
from . import views


urlpatterns = [
    path('products', views.product_list, name='products'),
    path('product/<int:product_id>/', views.product_detail, name='product')
]
