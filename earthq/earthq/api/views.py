from django.shortcuts import render
from .models import Data 
from .serializers import DataSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
class DataViewset(ModelViewSet):
    model = Data
    serializer_class = DataSerializer
    queryset = Data.objects.all()
