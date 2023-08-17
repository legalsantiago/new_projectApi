from django.contrib import admin
from app.products.models import Product,MeasureUnit,CategoryProduct,Indicador
# Registrar Models para admin y como se muestra data en interfaz

class MeasureUnitAdmin(admin.ModelAdmin):
    list_display = ('id','description')

class CategoryProductAdmin(admin.ModelAdmin):
    list_display = ('id','description')

admin.site.register(Product)
admin.site.register(MeasureUnit,MeasureUnitAdmin)
admin.site.register(CategoryProduct,CategoryProductAdmin)
admin.site.register(Indicador)

