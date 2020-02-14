from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
#from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from Profile2.models import Profile2, Ciudad, Estado, EstadoCivil, Genero, Ocupacion
from Profile2.serializer import Profile2Serializers, CiudadSerializers, EstadoSerializers, EstadoCivilSerializers, GeneroSerializers, OcupacionSerializers


class Profile2List(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Profile2.objects.filter(delete = False)
        serializer = Profile2Serializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Profile2Serializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class CiudadList(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Ciudad.objects.filter(delete = False)
        serializer = CiudadSerializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CiudadSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        

class EstadoList(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Estado.objects.filter(delete = False)
        serializer = EstadoSerializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class EstadoCivilList(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = EstadoCivil.objects.filter(delete = False)
        serializer = EstadoCivilSerializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EstadoCivilSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class OcupacionList(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Ocupacion.objects.filter(delete = False)
        serializer = OcupacionSerializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = OcupacionSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


class GeneroList(APIView):
    def get(self,request , formar=None):
        print("Metodo get filter")
        queryset = Genero.objects.filter(delete = False)
        serializer = GeneroSerializers(queryset , many = True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GeneroSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data 
            return Response(datas)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

