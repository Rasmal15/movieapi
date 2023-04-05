from django.shortcuts import render
from .models import *
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.


# Create your views here.
class Dishlist(APIView):
    def get(self,request,*args,**kwargs):
        return Response(data=dishes)
    def post(self,request,*args,**kwargs):
        data=request.data
        dishes.append(data)
        return Response(data=dishes)

class Dishitem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        dish=[i for i in dishes if i['id']==id].pop()
        return Response(data=dish)
    def put(self,request,*args,**kwargs):
        data=request.data
        id=kwargs.get("mid")
        dish=[i for i in dishes if i['id']==id].pop()
        dish.update(data)
        return Response(data=dishes)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("mid")
        dish=[i for i in dishes if i['id']==id].pop()
        dishes.remove(dish)
        return Response(data=dishes)