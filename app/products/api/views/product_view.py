from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from app.base.api import GeneralListApiView 
from app.products.api.serializers.product_serializer import ProductSerializers

class ProductListAPIview(GeneralListApiView):
    serializer_class = ProductSerializers
    

class ProductCreateAPIview(generics.CreateAPIView):
    serializer_class = ProductSerializers

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado'},status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    







