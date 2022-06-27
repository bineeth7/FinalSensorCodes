from django.urls import include
from django.urls import  path
from rest_framework.urlpatterns import format_suffix_patterns   
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'Data', views.DataViewset)

urlpatterns = [
path('', include(router.urls)),
]