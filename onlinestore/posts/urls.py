
from django.urls import path
from .views import *

urlpatterns = [
    path('', hello),
    path('date/', now_date),
    path('goodby/', goodby)
]