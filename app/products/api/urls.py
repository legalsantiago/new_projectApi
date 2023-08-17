from django.urls import path
from app.products.api.views.general_view import MeasureUnitListAPIview,IndicatorListAPIview,CategoryProductListAPIview
from app.products.api.views.product_view import ProductListAPIview, ProductCreateAPIview

urlpatterns = [
   path('measure_unit/',MeasureUnitListAPIview.as_view(),name='measure_unit'),
   path('category_product/',CategoryProductListAPIview.as_view(),name='Categoria_product'),
   path('indicator/',IndicatorListAPIview.as_view(),name='indicador_oferta'),
   path('product/list/',ProductListAPIview.as_view(), name='Products_list'),
   path('product/create/',ProductCreateAPIview.as_view(), name='Products_create')
]