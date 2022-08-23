from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):        
    
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'user_type', 'password']
        extra_kwargs = {
            'password' : {'write_only': True},
        }
        
        
# class LoginSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username','email','password']
#         extra_kwargs = {
#             'email':{'read_only':True}
#         }