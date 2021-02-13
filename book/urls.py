from django.urls import path
from .views import *

urlpatterns = [
    path('', BookView, name= 'viewbook'),
    path('test/', Test, name= 'index'),
]