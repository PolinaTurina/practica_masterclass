from django.contrib import auth
from django.shortcuts import render, redirect

from . forms import RegisterForm


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
    return auth.logout(request)

def profile(request):
    return render(request, 'auth/profile.html')
