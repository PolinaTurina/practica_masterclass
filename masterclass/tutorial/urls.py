from . import views
from django.urls import path

from .views import *

app_name = 'tutorial'

urlpatterns = [
    path('', TutorialView.as_view(), name='full'),
]
