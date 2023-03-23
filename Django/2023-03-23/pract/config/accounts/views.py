from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import CustomUserChangeForm, CustomUserCreationForm

# Create your views here.
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        print('>>>')
        if form.is_valid:
            print('<<<')
            print(form)
            print(form.get_user())
            auth_login(request, form.get_user())
            return redirect('todos:index')
    else:
        form = AuthenticationForm()
    
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    
    return redirect('todos:index')

def signup(request):
    if request.method == "POST":
        
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save()
            auth_login(request, user)
            return redirect('todos:index')
   
    else:
        form = CustomUserCreationForm
    context = {
        'form' : form,
    }

    return render(request, 'accounts/signup.html', context)