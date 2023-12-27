from django.urls import path
from apps.core.views import *

urlpatterns = [
  path('home', home, name='home'),
  path('jobs', jobs, name='jobs'),
  # path('home/', home, name='home'),
]