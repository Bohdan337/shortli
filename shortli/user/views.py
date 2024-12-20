from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import login as login_view, authenticate, logout


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(user)
            login_view(request, user)
            return redirect('main')
    else:
        form = SignUpForm()
    
    return render(request, 'auth/signup.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid(): 
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login_view(request, user)  
                return redirect('main')  
            else:
                form.add_error(None, "Неправильний логін або пароль")
    else:
        form = LoginForm()
    return render(request, 'auth/login.html', {'form': form}) 


def logout_view(request):
    logout(request)
    return redirect('main')