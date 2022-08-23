from django.shortcuts import render
from .models import User
from rest_framework import generics
from .serializers import UserSerializer
from rest_framework import mixins
from rest_framework.exceptions import AuthenticationFailed
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import APIView
import jwt, datetime



# Create your views here.

class createViewAccount(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
class editDeleteAccount(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
# class loginUser(generics.GenericAPIView, mixins.CreateModelMixin):
#     serializer_class = LoginSerializer
    
#     def post(self, request):
#         username = request.data['username']
#         password = request.data['password']
        
#         user = User.objects.filter(username=username).first()
#         if user is None:
#             raise AuthenticationFailed('User not found')
        
#         if not user.check_password(password):
#             raise AuthenticationFailed('password is incorrect')
        
#         payload = {
#             'id':user.id,
#             'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=5),
#             'iat': datetime.datetime.utcnow()
#         }
        
#         token = jwt.encode(payload,'secret', algorith='HS256')#decode('utf-8')
#         response = Response()
#         response.set_cookies(key='jwt',value=token, httponly=True)
#         response.data = {
#             'jwt' : token
#         }
#         return response
        
    
# class Logged_in_user(APIView):
#     def get(self, request):
#         token = request.COOKIES.get('jwt')
#         if not token:
#             raise AuthenticationFailed('Unauthenticated')
#         try:
#             payload = jwt.decode(token,'secret',algorithms=['HS256'])
            
#         except jwt.ExpiredSignatureError:
#             raise AuthenticationFailed('Unauthenticated')
        
#         user = User.objects.filter(id=payload['id']).first()
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
# class Log_out(APIView):
#     def post(self, request):
#         response = Response()
#         response.delete_cookie('jwt')
#         response.data = {
#             'message':'Logged out successfully'
#         }
        
#         return response