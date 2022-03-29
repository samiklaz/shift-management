from django.urls import path
from core.views import *

app_name = 'core'
urlpatterns = [
    path('', IndexAPIView.as_view(), name='index'),
]