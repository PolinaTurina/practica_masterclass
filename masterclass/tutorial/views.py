from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from . models import *

# class TutorialView(ListView):
#     template_name = 'tutorial/full.html'
#     model = Category
#     context_object_name = 'category_list'
def tutorial_view(request):
    category = Category.objects.all()
    masterclass = MasterClass.objects.all()
    context = {'category': category, 'masterclass': masterclass}
    return render(request, 'tutorial/full.html', context)

def tutorial_list(request, pk):
    category = Category.objects.all()
    masterclass = MasterClass.objects.filter(category__pk=pk)
    context = {'category': category, 'masterclass': masterclass}
    return render(request, 'tutorial/full.html', context)

