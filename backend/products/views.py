from rest_framework import generics,status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    def perform_create(self,serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None

        if content is None:
            content = title

        

        serializer.save(content = content)


class ProductDetailAPTView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPTView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



class ProductDestroyAPTView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

@api_view(["GET","POST"])
def product_alt_view(request,pk=None,*args,**kwargs):
    method = request.method

    if method == "GET":
        if pk is not None:
            obj = get_object_or_404(Product,pk=pk)
            data = ProductSerializer(obj,many=False).data
            return Response(data)
        queryset = Product.objects.all()
        data = ProductSerializer(queryset,many=True).data
        return Response(data)

    if method == "POST":
        serializer = ProductSerializer(data = request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None

            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



