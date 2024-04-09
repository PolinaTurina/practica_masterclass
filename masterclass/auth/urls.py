# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy
# from django.views.generic import CreateView
from . import views
from .forms import LoginForm

app_name = 'custom_auth'

urlpatterns = [
    # path('login/', LoginView.as_view(template_name='auth/login.html',
    #                                  ), name='login'),
    path('login/', LoginView.as_view(template_name='auth/login.html',
                                     authentication_form=LoginForm), name='login'),
    # path('register/', CreateView.as_view(template_name='auth/register.html',
    #                             success_url=reverse_lazy('auth:login'),
    #                             form_class=UserCreationForm, model=User),
    #                             name='register'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
]
