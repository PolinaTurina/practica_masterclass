from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from . models import *


# def tutorial_full(request):
#
#     return render(request, 'tutorial/full.html')

class TutorialView(ListView):
    template_name = 'tutorial/full.html'
    model = Category
    context_object_name = 'category_list'