from app.base.api import GeneralListApiView
#from app.products.models import MeasureUnit,Indicador,CategoryProduct
from app.products.api.serializers.general_serializers import MeasureUnitSerializer,CategoryProductSerializer,IndicadorSerializer
 
class MeasureUnitListAPIview(GeneralListApiView):
    serializer_class=MeasureUnitSerializer

    # def get_queryset(self):
    #     return MeasureUnit.objects.filter(status=True)
class IndicatorListAPIview(GeneralListApiView):
    serializer_class = IndicadorSerializer


class CategoryProductListAPIview(GeneralListApiView):
    serializer_class = CategoryProductSerializer
    






