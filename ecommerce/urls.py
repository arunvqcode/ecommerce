
from django.contrib import admin
from django.urls import path,include
from cart.urls import router as cart_router
from django.conf import settings  
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('user_app.urls')),
    path('', include(cart_router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


