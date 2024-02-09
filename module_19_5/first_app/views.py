from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm,SetPasswordForm
# Create your views here.

def home(request):
    return render(request, 'base.html')

def profile(request):
        return render(request, 'profile.html')
    

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account created Successfully")
            form.save()
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'signup.html', {'form':form})
    

def user_login(request):
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=name, password=user_pass)
                if user is not None:
                    messages.success(request, "Logged in Successfully")
                    login(request, user)
                    return redirect('profile')
                else:
                    messages.warning(request, "Login information incorrect")
                    return redirect('signup')
        else:
            form = AuthenticationForm()

        return render(request, 'login.html', {'form': form})

        


def user_logout(request):
        logout(request)
        return redirect('user_login')
  
    

def pass_change1(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PasswordChangeForm(user = request.user, data = request.POST)
            if form.is_valid():
                messages.success(request, "Password updated Successfully")
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
            
        else:
            form = PasswordChangeForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    else : 
        return redirect('signup')
    


def pass_change2(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = SetPasswordForm(user = request.user, data = request.POST)
            if form.is_valid():
                messages.success(request, "Password updated Successfully")
                form.save()
                update_session_auth_hash(request, form.user)
                return redirect('profile')
        else:
            form = SetPasswordForm(user=request.user)
        return render(request, 'pass_change.html', {'form':form})
    else : 
        return redirect('signup')