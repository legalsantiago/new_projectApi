from rest_framework import serializers
from app.users.models import User

"""SERIALIZADOR GET ALL"""
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        #fields = ['id','username','last_name','email','password']
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id':instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'last_name': instance['last_name']
        }

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
    def update(self, instance, validated_data):
        update_user = super().update(instance, validated_data)
        update_user.set_password(validated_data['password'])
        update_user.save()
        return update_user


"""SERIALIZADOR USO GET PUT FOR ID"""
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        #fields = ['id','username','last_name','email','password']
        fields = '__all__'

    def to_representation(self,instance):
        return{
            'id':instance.id,
            'username': instance.username,
            'last_name': instance.last_name,
            'email': instance.email,
            'password': instance.password
        }
    
        




class TestUserSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 200)
    email = serializers.EmailField()

    def validate_name(self,value):
       
        if 'none' in value:
            raise serializers.ValidationError('Error, no puede exitir un usuario con ese nombre')
        return value
    
    def validate_email(self,value):
        if value == '': 
            raise serializers.ValidationError("error, necesitas completar este campo")
        return value


    #AL ENVIAR LA PROPIEDAD CONTEXT COMO PARAMETRO PUEDO RELACIONAR INFORMACION DENTRO DE UN SERIALIZER PARA VALIDAR INFO
    
    
    #METODOS GENERALES QUE SE UTILIZAN DE MANERA AUTOMATICA POR SERIALIZER FIELD= __ALL__
    def validate(self, value):
        return value

    def create(self, validated_data):
        return User.objects.create(**validated_data)
    
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.email = validated_data.get('email', instance.email)
    #     instance.save()
    #     return instance
 
    
        