from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login
from .forms import CreationUserForm,LoginUserForm
# Create your views here.

def users_view(request):
    if request.method == "POST":
        form = CreationUserForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("home:index")
    else:
        form = CreationUserForm()
    return render(request, 'users/users.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect("home:index")
    else:
        form = LoginUserForm()
    return render(request, 'users/login.html', {'form':form})
