from django.urls import path
from apps.common.views import *

urlpatterns = [
  path('common/', common, name='common'),
]