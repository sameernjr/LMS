from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import login, logout
from .forms import CreationUserForm,LoginUserForm
# Create your views here.

# def admin_required(view_func):
#     def wrap(request, *args, **kwargs):
#         if request.user.is_superuser:
#             return view_func(request, *args, **kwargs)
#         else:
#             messages.error(request, "You are not authorized to access this page.")
#             return redirect(reverse('home:index'))
#     return wrap


def registration_view(request):
    if request.method == "POST":
        form = CreationUserForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, form.save())
            return redirect("users:login")
    else:
        form = CreationUserForm()
    return render(request, 'registration/users.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, form.get_user())
            return redirect("home:index")
    else:
        form = LoginUserForm()
    return render(request, 'registration/login.html', {'form':form})

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("users:login")
    