from django.db import models
from simple_history.models import HistoricalRecords
from app.base.models import BaseModel
#MEDIDAS DE UNIDAD
class MeasureUnit(BaseModel):
    description = models.CharField('Descripcion',max_length=50, blank=False,null=False,unique=True)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    
    class Meta:
        verbose_name = 'MeasureUnit'
        verbose_name_plural = 'MeasureUnits'

    def __str__(self) -> str:
        return self.description

class CategoryProduct(BaseModel):

    description = models.CharField("descripcion", max_length=50,unique=True,null=False,blank=False)
    historical = HistoricalRecords()

    @property
    def _history_user(self):
        return self.changed_by

    @_history_user.setter
    def _history_user(self,value):
        self.changed_by = value
    

    class Meta:
        verbose_name = "Categoria de Producto"
        verbose_name_plural = "Categorias de Productos"

    def __str__(self):
        return self.description

#MODELO DE OFERTAS VARIABLE
class Indicador(BaseModel):
    descuento_value = models.PositiveSmallIntegerField(default=0)
    fk_category_product=models.ForeignKey(CategoryProduct, verbose_name=("Indicador de oferta"), on_delete=models.CASCADE)
    historical=HistoricalRecords()

    class Meta:
        verbose_name = "Indicador de Oferta"
        verbose_name_plural = "Indicadores de Ofertas"

    def __str__(self):
        return f'Ofeta de la categoria {self.category_product} : {self.descuento_value}%'
    
class Product(BaseModel):

    name_product = models.CharField(max_length=100,unique=True,null=False,blank=False)
    description = models.TextField('Descripcion de producto', blank=False,null=False)
    imagen = models.ImageField("imagen del producto", upload_to='products/',blank= True, null=True)
    fk_measuret_unit=models.ForeignKey(MeasureUnit,on_delete=models.CASCADE,verbose_name='Unida De Medida',null=True)
    fK_category_product=models.ForeignKey(CategoryProduct, verbose_name=("Categoria de producto"), on_delete=models.CASCADE,null=True)
    historical=HistoricalRecords()

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural ="Productos"

    def __str__(self):
        return self.name_product 
    
    
    






    










