from . import views
from django.urls import path

from .views import *

app_name = 'tutorial'

urlpatterns = [
    # path('', TutorialView.as_view(), name='full'),
    path('', tutorial_view, name='full'),

    path('<int:pk>/', tutorial_list, name='tutorial'),
    path('detail/<int:pk>/', tutorial_detail, name='detail'),

    path('', bron, name='bron'),
]
