from rest_framework import serializers
from . import models


class ConductoresSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = models.Conductores


class CarrosSerializer(serializers.ModelSerializer):

    conductor = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombres'
    )

    propietario = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombres'
    )

    class Meta:
        fields = '__all__'
        model = models.Carros


class PolizasSerializer(serializers.ModelSerializer):

    carro = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre'
    )

    class Meta:
        fields = '__all__'
        model = models.Polizas


class PropietariosSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Propietarios


class TipoGastoSerializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.TipoGasto


class RentasSerializer(serializers.ModelSerializer):

    carro = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='nombre'
    )

    class Meta:
        fields = '__all__'
        model = models.Renta
