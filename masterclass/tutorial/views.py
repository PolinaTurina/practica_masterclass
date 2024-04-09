from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView
from django.db.models import Q

from .forms import BronForm, FilterForm
from . models import *

# class TutorialView(ListView):
#     template_name = 'tutorial/full.html'
#     model = Category
#     context_object_name = 'category_list'

# вывод главной страницы с категориями
# def tutorial_view(request):
#     category = Category.objects.all()
#     masterclass = MasterClass.objects.all()
#     context = {'category': category, 'masterclass': masterclass}
#     return render(request, 'tutorial/full.html', context)

def tutorial_view(request):
    category = Category.objects.all()
    masterclass = MasterClass.objects.all()

    form = FilterForm()
    # Обработка фильтрации
    if 'filter' in request.GET:
        filter_option = request.GET['filter']
        if filter_option == '1':
            masterclass = masterclass.order_by('price')
        elif filter_option == '2':
            masterclass = masterclass.order_by('-price')
        elif filter_option == '3':
            masterclass = MasterClass.objects.all()

    context = {'category': category, 'masterclass': masterclass, 'form':form}
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
    else:
        form = BronForm(initial={'count': 1})

    context = {
        'masterclass': masterclass,
        'form': form
    }
    return render(request, 'tutorial/detail.html', context)
