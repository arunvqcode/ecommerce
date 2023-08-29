
from django.urls import path
from rest_framework.routers import DefaultRouter,SimpleRouter
from.views import *

router = SimpleRouter()


router.register('product',ProductDetailsViewSet, basename="product")
router.register('cart/add',AddToCartViewSet,basename='add-to-cart')
router.register('cart', CartViewSet, basename='view-cart')


