from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def users_view(request):
    form = UserCreationForm()
    return render(request, 'users/users.html', {'form':form})
