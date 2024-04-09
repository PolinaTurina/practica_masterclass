from django.contrib import auth
from django.shortcuts import render, redirect

from . forms import RegisterForm
from tutorial.models import Bron


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('auth:login')
    context = {'form': form}
    return render(request, 'auth/register.html', context)


# test123qwerty
# test123qwertyA
def logout(request):
    auth.logout(request)
    return redirect('tutorial:full')
    # return auth.logout(request)

def profile(request):
    # bron = Bron.objects.all()
    user_id = request.user.id
    bron = Bron.objects.filter(user_id=user_id).distinct()
    context = {'bron': bron}
    return render(request, 'auth/profile.html', context)
