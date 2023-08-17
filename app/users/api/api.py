#from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view #import decorator is simple
from app.users.api.serializers import UserSerializer, UserListSerializer
from app.users.api.serializers import User
from rest_framework import status
#### VIEWS Y TOMA Y ENTREGA DE DATOS 

@api_view(['GET','POST'])
def user_api_view(request,pk=None):
    
    if request.method == 'GET':
        users = User.objects.all().values('id','username','last_name','email') #consulta similar select * from
        users_serializer = UserSerializer(users, many=True) #ejecuto consulta y recibo con atributo many=true all data serializada a json.
        return Response(users_serializer.data, status=status.HTTP_200_OK)#retorno los datos con su propiedad data
    
    elif request.method == 'POST':
        users_serializer = UserSerializer(data = request.data,id=pk)#envio al serializador proceso inverso
        
        if users_serializer.is_valid():
            users_serializer.save()#salvar info en bd
            return Response({'message':'Usuario creado correctamente!'}, status=status.HTTP_201_CREATED)
        return Response(users_serializer.errors, status=status.HTTP_400_BAD_REQUEST)  #RETORNO DE INFO SOBRE LAS ACCIONES QUE SE EJECUTAN

@api_view(['GET','PUT','DELETE'])
def user_detail_view(request,pk=None,username1=None):
    # QUERY.SET
    user = User.objects.filter(id=pk,username=username1).first()
    
    if user:
        if request.method == 'GET':
            #user = User.objects.get(id=pk) <--- otra manera de filtrar info buscar
            user_Serializer = UserListSerializer(user)
           
            return Response(user_Serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            user_Serializer = UserSerializer(user,data=request.data)#al pasar las 2 INSTANCIAS y la info se entiende una actualizacion.
            if user_Serializer.is_valid():
                user_Serializer.save()
                return Response(user_Serializer.data, status= status.HTTP_200_OK)
            return Response(user_Serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':"Usuario eliminado con exito" },status=status.HTTP_200_OK)
    else:
        return Response({'message':'No se encontro el usuario'}, status=status.HTTP_404_NOT_FOUND)
    
    
        

    


