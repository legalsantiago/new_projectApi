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
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Producto creado'},status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class ProductRetrieveAPIview(generics.RetrieveAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status = True)
    
class ProductDestroyAPIview(generics.DestroyAPIView):
    serializer_class = ProductSerializers

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(status = True)
    
    def delete(self,request,pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.status = False
            product.save()
            return Response({'message':'Producto Eliminado'}, status=status.HTTP_200_OK)
        else:
            return Response({'message':'No Existen Coincidencias'},status=status.HTTP_400_BAD_REQUEST)

# class ProductUpdateAPIview(generics.UpdateAPIView):
    
#     serializer_class = ProductSerializers
    
#     def get_queryset(self,pk):
#         return self.get_serializer().Meta.model.objects.filter(status = True).filter(id=pk).first()
    
#     def patch(self, request,pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk))
#             return Response(product_serializer.data, status=status.HTTP_200_OK)
#         else:
#             return Response({'Error':'No existe un producto con estos datos'},status=status.HTTP_400_BAD_REQUEST) 
        
#     def put(self, request, pk=None):
#         if self.get_queryset(pk):
#             product_serializer = self.serializer_class(self.get_queryset(pk),data = request.data)
#             if product_serializer.is_valid():
#                 product_serializer.save()
#                 Response(product_serializer.data,status=status.HTTP_200_OK)
#             else:
#                 Response(product_serializer.errors,status=status.HTTP_400_BAD_REQUEST)


        


        
            

    

    







