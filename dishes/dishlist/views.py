from django.shortcuts import render
from .models import *
from .serializer import Dishser
from rest_framework import status
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


class DishModelList(APIView):
    def get(self,request,*args,**kwargs):
        dish=Dishes.objects.all()
        dser=Dishser(dish,many=True)
        return Response(data=dser.data)
    def post(self,request,*args,**kwargs):
        dish=request.data
        ser=Dishser(data=dish)
        if ser.is_valid():
            ser.save()
            return Response({"msg":"created"})
        else:
            return Response({"msg":ser.errors},status=status.HTTP_404_NOT_FOUND)

class DishMItem(APIView):
    def get(self,request,*args,**kwargs):
        id=kwargs.get('did')
        try:
            dish=Dishes.objects.get(id=id)
            dser=Dishser(dish)
            return Response(dser.data)
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,*args,**kwargs):
        id=kwargs.get("did")
        try:
            dish=Dishes.objects.get(id=id)
            dish.delete()
            return Response({"msg":"deleted"})
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,*args,**kwargs):
        id=kwargs.get("did")
        try:
            dish=Dishes.objects.get(id=id)
            ser=Dishser(data=request.data,instance=dish)
            if ser.is_valid():
                ser.save()
                return Response({"msg":"updated"})
            else:
                return Response({"msg":ser.errors},status=status.HTTP_422_UNPROCESSABLE_ENTITY)
        except:
            return Response({"msg":"invalid id"},status=status.HTTP_400_BAD_REQUEST)

