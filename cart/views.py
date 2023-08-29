from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework.response import Response
from django.shortcuts import get_object_or_404,render
from rest_framework import status
from .permissions import *


class ProductDetailsViewSet(viewsets.ModelViewSet):
    queryset = ProductDetails.objects.all()
    serializer_class = ProductDetailsSerializer
    permission_classes = [IsAdminOrReadOnly]
    

class AddToCartViewSet(viewsets.ModelViewSet):
    serializer_class = ProductDetailsSerializer
    queryset = ProductDetails.objects.all()

    def create(self, request):
        user = request.user
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity', 1)

        try:
            product = ProductDetails.objects.get(pk=product_id)
        except ProductDetails.DoesNotExist:
            return Response({'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)

        cart, created = Cart.objects.get_or_create(user=user)
        cart_item, _ = CartItem.objects.get_or_create(cart=cart, product=product)
        cart_item.quantity += int(quantity)
        cart_item.save()

        return Response({'message': 'Product added to cart successfully.'}, status=status.HTTP_201_CREATED)


class CartViewSet(viewsets.ModelViewSet):
    serializer_class = CartItemSerializer
    queryset = CartItem.objects.all()

    def list(self, request):
        user = request.user
        try:
            cart = Cart.objects.get(user=user)
            cart_items = CartItem.objects.filter(cart=cart)
            serializer = self.get_serializer(cart_items, many=True)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found.'}, status=status.HTTP_404_NOT_FOUND)





# class ProductViewSet(viewsets.ViewSet):
#     # permission_classes = [IsAdminUser]
    
#     def create(self,request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors)
        
        
#     def list(self, request):
#         queryset = ProductDetails.objects.all()
#         serializer = ProductSerializer(queryset, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)
    
    
#     def retrieve(self, request, pk=None):
#         queryset = ProductDetails.objects.all()
#         product = get_object_or_404(queryset, pk=pk)
#         serializer = ProductSerializer(product, many=True)
#         return Response(serializer.data,status=status.HTTP_200_OK)

#     def update(self, request, pk=None):
#         product = ProductDetails.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def partial_update(self, request, pk=None):
#         product = ProductDetails.objects.get(pk=pk)
#         serializer = ProductSerializer(product, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):
#         product = ProductDetails.objects.get(pk=pk)
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

