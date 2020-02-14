from rest_framework import routers, serializers, viewsets


#--------------------AGREGANDO MODELOS------------------------

from Profile2.models import Profile2, Ciudad, Estado, EstadoCivil, Ocupacion, Genero

class Profile2Serializers(serializers.ModelSerializer):
    class Meta:
        model = Profile2
        fields = ('__all__')


class CiudadSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ciudad
        fields = ('__all__')

class EstadoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = ('__all__')


class EstadoCivilSerializers(serializers.ModelSerializer):
    class Meta:
        model = EstadoCivil
        fields = ('__all__')


class OcupacionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = ('__all__')

class GeneroSerializers(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = ('__all__')