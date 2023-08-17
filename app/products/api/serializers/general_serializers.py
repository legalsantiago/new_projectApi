from app.products.models import MeasureUnit,Indicador,CategoryProduct
from rest_framework import serializers

class MeasureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasureUnit
        exclude = ('status','create_date')

class IndicadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indicador
        exclude = ('status','create_date')

class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryProduct
        exclude = ('status','create_date',)

  