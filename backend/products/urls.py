from django.urls import path

from . import views


urlpatterns = [
    path("/<int:pk>/",views.ProductDetailAPTView.as_view(),name='product-detail'),
    path("<int:pk>/update/",views.ProductUpdateAPTView.as_view(),name='product-edit'),
    path("<int:pk>/delete/",views.ProductDestroyAPTView.as_view()),
    path("",views.ProductListCreateAPIView.as_view(),name = 'product-list')
]