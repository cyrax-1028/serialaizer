from django.urls import path
from myapp import views

urlpatterns = [
    path('categories/', views.CategoryListView.as_view(), name='category-list'),
    path('categories/<int:pk>/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('products/', views.ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('product-images/', views.ImagesListView.as_view(), name='product-image-list'),
    path('product-images/<int:pk>/', views.ImageDetailView.as_view(), name='product-image-detail'),
]