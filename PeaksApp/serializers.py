from rest_framework import serializers
from .models import Peaks


class PeakSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Peaks
        fields = ['url', 'id', 'name', 'lat', 'long', 'altitude']

