from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView

from .forms import BronForm
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
    # masterclass = MasterClass.objects.get(pk=pk)
    # context = {'masterclass': masterclass}
    # return render(request, 'tutorial/detail.html', context)

    masterclass = MasterClass.objects.get(pk=pk)

    if request.method == 'POST':
        form = BronForm(request.POST)
        if form.is_valid():
            booking_instance = form.save(commit=False)
            booking_instance.user_id = request.user
            booking_instance.masterclass_id = masterclass
            booking_instance.status = 0
            booking_instance.save()
            # Дополнительная обработка/логика при необходимости
    else:
        form = BronForm(initial={'count': 1})

    context = {
        'masterclass': masterclass,
        'form': form
    }
    return render(request, 'tutorial/detail.html', context)


# def booking_handler(request):
#     if request.method == 'POST':
#         form = BronForm(request.POST)
#         if form.is_valid():
#             booking_instance = form.save(commit=False)
#             booking_instance.status = 0
#             booking_instance.save()
#             # Additional handling/logic here if needed
#     else:
#         form = BronForm()
#
#     return render(request, 'tutorial/detail.html', {'form': form})
