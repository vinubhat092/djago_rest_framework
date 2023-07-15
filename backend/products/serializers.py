from rest_framework import serializers
from rest_framework.reverse import reverse
from .validators import validate_title_no_hello
from .models import Product
from . import validators
class ProductSerializer(serializers.ModelSerializer):
    my_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(view_name = 'product-detail',lookup_field = 'pk')
    title = serializers.CharField(validators=[validators.validate_title_no_hello,
                                              validators.unique_product_title])
    class Meta:
        model = Product
    
        fields = [
            'user',
            'url',
            'edit_url',
            'pk',
            'title',
            'content',
            'price',
            'sale_prize',
            'my_discount'

        ]
    # def validate_title(self,value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user,title__iexact = value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} already exists")
    #     return value
    # def create(self, validated_data):
    #     # email = validated_data.pop('email')
    #     obj = super().create(validated_data)
    #     return obj

    # def update(self,instance,validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance,validated_data)

    def get_edit_url(self,obj):
        print("fef",obj)
        # return f"/api/products/{obj.pk}"
        print("cotet",self.context)
        request = self.context.get('request')
        print("request",request)
        if request is None:
            return None
        return reverse("product-edit",kwargs={'pk':obj.pk},request=request)

    def get_my_discount(self,obj):
        try:
            return obj.get_discount()
        except:
            return None
