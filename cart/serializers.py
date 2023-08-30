from rest_framework import serializers
from .models import *



class ProductDetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductDetails
        fields = '__all__'


        
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductDetailsSerializer() 
    class Meta:
        model = CartItem
        fields = ['product', 'quantity']
        

class AddToCartSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField(min_value=1, required=False, default=None)





