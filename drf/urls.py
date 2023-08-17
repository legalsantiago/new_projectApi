"""
URL configuration for drf project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from rest_framework.documentation import include_docs_urls
from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
   openapi.Info(
      title="Swagger Api",
      default_version='v1',
      description="Test Swagger documentation",
      terms_of_service="http://127.0.0.1:8000/",
      contact=openapi.Contact(email="santiagotriunfobet1@gmail.com"),
    #   license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)
#url FALTANTE
urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include('app.users.api.urls')),
    path('products/',include('app.products.api.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('docs/',include_docs_urls(title = 'api Documentation')),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   
]

