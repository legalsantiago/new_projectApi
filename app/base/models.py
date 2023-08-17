from django.db import models

class BaseModel(models.Model):

    id = models.AutoField(primary_key=True)
    status = models.BooleanField('estado',default=True)
    create_date = models.DateField('fecha de creacion', auto_now=False,auto_now_add=True)
    modificate_day = models.DateField('fecha de modificacion', auto_now=True,auto_now_add=False)
    delete_day = models.DateField("fecha de eliminacion", auto_now=False, auto_now_add =True)

    class Meta:
        abstract= True
        verbose_name = 'Modelo Base'
        verbose_name_plural = 'Modelos Bases'
