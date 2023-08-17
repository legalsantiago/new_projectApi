from app.products.models import Product
from rest_framework import serializers
#from app.products.api.serializers.general_serializers import MeasureUnitSerializer, CategoryProductSerializer
#LLAMANDO A LA CLASE DEL SERIALIZADOR DE LA FK PUEDO MOSTRAR LOS DATOS QUE NECESITE
#LLAMANDO
class ProductSerializers(serializers.ModelSerializer):

    
    #fK_category_product = serializers.StringRelatedField()
    #fk_measuret_unit = serializers.StringRelatedField()

    class Meta:
        model = Product
        exclude = ('status','create_date','delete_day')
     
    def to_representation(self, instance):
        return {
            'name_product':instance.name_product,
            'description':instance.description,
            'imagen':instance.imagen if instance.imagen != '' else '',
            'fK_category_product':instance.fK_category_product.description,
            'fk_measuret_unit':instance.fk_measuret_unit.description

        }
    



   