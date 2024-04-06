from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView, DetailView

from . models import *

# class TutorialView(ListView):
#     template_name = 'tutorial/full.html'
#     model = Category
#     context_object_name = 'category_list'


# вывод главной страницы с категориями
def tutorial_view(request):
    category = Category.objects.all()
    masterclass = MasterClass.objects.all()
    context = {'category': category, 'masterclass': masterclass}
    return render(request, 'tutorial/full.html', context)


# фильтрация мастер классов по категорями на этой же главной странице
def tutorial_list(request, pk):
    category = Category.objects.all()
    masterclass = MasterClass.objects.filter(category__pk=pk)
    context = {'category': category, 'masterclass': masterclass}
    return render(request, 'tutorial/full.html', context)


# переход на детали мастеркласса
def tutorial_detail(request, pk):
    masterclass = MasterClass.objects.get(pk=pk)
    context = {'masterclass': masterclass}
    return render(request, 'tutorial/detail.html', context)