from rest_framework import serializers
from .models import GeoAddress


class GeoAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeoAddress
        fields = ('id', 'country', 'city', 'street','latitude','longitude','count')
