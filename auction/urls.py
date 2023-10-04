from django.urls import path
from . import views

urlpatterns = [
    path('', views.ItemListView.as_view(), name='auction-home'),
    path('post/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('post/<int:pk>/', views.ProductDetailView.as_view(), name='post-detail'),
    path('post/<int:pk>/update/', views.ProductUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-delete'),
    path('post/product/', views.ProductCreateView.as_view(), name='product-create'),
    path('about', views.about, name='auction-about'),
]