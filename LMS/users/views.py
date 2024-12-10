from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Create your views here.

def users_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home:index")
    else:
        form = UserCreationForm()
    return render(request, 'users/users.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            #LOGIN HERE
            return redirect("home:index")
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form':form})
