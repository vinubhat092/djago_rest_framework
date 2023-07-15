from rest_framework import generics,status,mixins,permissions,authentication
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer
from django.shortcuts import get_object_or_404
from api.permissions import IsStaffEditorPermission
from api.authentication import TokenAuthentication
from api.mixins import StaffEditorPermissionMixin
class ProductListCreateAPIView(
    StaffEditorPermissionMixin,
    generics.ListCreateAPIView):
    print("dsdfe")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # authentication_classes = [authentication.SessionAuthentication,
    #                           TokenAuthentication]
    # permission_classes = [IsStaffEditorPermission]      #we can use decorators for permissions in func based view(IsAuthenticatedOrReadOnly,DjangoModelPermissions)
    def perform_create(self,serializer):
        print("dsds")
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        
        if content is None:
            content = title

        serializer.save(user = self.request.user,content = content)

    def get_queryset(self,*args,**kwargs):
        qs = super().get_queryset(*args,**kwargs)
        request = self.request
        user = request.user
        if not user.is_authenticated:
            return Product.objects.none()
        return qs.filter(user = request.user)


class ProductDetailAPTView(StaffEditorPermissionMixin,generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductUpdateAPTView(StaffEditorPermissionMixin,generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    

    def perform_update(self,serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title



class ProductDestroyAPTView(StaffEditorPermissionMixin,generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self,instance):
        super().perform_destroy(instance)

class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):                                                        #clsss based views with mixins which has many builtin packages handy
    print("jfkefe")
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
    def get(self,request, *args, **kwargs):   
        print("effe",args,kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request,*args,**kwargs)             #no need of seperatly writing condition for post and get, directl ryt func with get or post
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)



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



