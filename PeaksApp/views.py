import django_filters
from django.shortcuts import render
from rest_framework import viewsets

from .models import Peaks
from .serializers import PeakSerializer


class PeakViewSet(viewsets.ModelViewSet):
    serializer_class = PeakSerializer
    queryset = Peaks.objects.all()


def index(request):
    return render(request, 'index.html')


class PeaksFilter(django_filters.FilterSet):
    class Meta:
        model = Peaks
        fields = {
            'lat': ['lt', 'gt'],
            'long': ['lt', 'gt'],
        }


def peak_list(request):
    f = PeaksFilter(request.GET, queryset=Peaks.objects.all())
    return render(request, 'filter.html', {'filter': f})
