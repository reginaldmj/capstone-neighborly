from rest_framework_gis.serializers import GeoFeatureModelSerializer
from rest_framework import serializers
from location.models import Neighborhood


class NeighborhoodSerializer(ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = '__all__'