from django.shortcuts import render
from rest_framework import generics
from .models import Class, Student
from WebApp.serializer import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.authtoken.models import Token
from django.http import HttpResponseRedirect

class RegisterUser(APIView):
    def post(self,request):
        serializer=Userserializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
            return Response({'status':403,'errors':serializer.errors,'message':'something wrong'})
        serializer.save()
        user=User.objects.get(username=serializer.data['username'])
        token_obj,_=Token.objects.get_or_create(user=user)
        return Response({'status':200,'payload':serializer.data,'token':str(token_obj),'message':'your data sent successfully'})



# Create your views here.

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentApi(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        stud_objs=Student.objects.all()
        serializer=StudentSerializer(stud_objs,many=True)
        print(request.user)
        return Response({'status':200,'payload':serializer.data})
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status':403,'errors':serializer.errors,'message':'something Went Wrong'})
        
        serializer.save()
        return Response({'status':200,'payload':serializer.data,'message':'your data submit successfully'})

    

    def patch(self,request):
        try:
            stud_objs=Student.objects.get(id=request.data['id'])
            serializer=StudentSerializer(stud_objs,data=request.data,partial=True)
            if not serializer.is_valid():
                print(serializer.errors)
                return Response({'status':403,'errors':serializer.errors,'message':'something went wrong'})
            
            serializer.save()
            return Response({'status':200,'payload':serializer.data,'message':'your data updated successfully'})
        
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})
        

    def delete(self,request):
        try:
            id=request.GET.get('id')
            stud_obj=Student.objects.get(id=id)
            stud_obj.delete()
            return Response({'status':200,'message':'deleted'})
        except Exception as e:
            print(e)
            return Response({'status':403,'message':'invalid id'})



