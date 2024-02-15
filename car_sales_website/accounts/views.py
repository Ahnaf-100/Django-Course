from django.shortcuts import render, redirect
from .forms import RegistrstionForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from . import forms
from orders.models import Order
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.utils.decorators import method_decorator


def signup(request):
    if request.method == 'POST':
        form = RegistrstionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrstionForm()
    return render(request, 'register.html', {'form': form, 'type' : 'Register'})

@login_required
def profile(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'profile.html', {'orders': orders})


@method_decorator(login_required, name='dispatch')
class ProfileView(DetailView):
    template_name = 'profile.html'
    context_object_name = 'orders'  
    def get_object(self):
        return Order.objects.filter(user=self.request.user)


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['username']  # Use square brackets
            user_pass = form.cleaned_data['password']  # Use square brackets
            user = authenticate(username=user_name, password=user_pass)
            if user is not None:
                messages.success(request, 'Logged in successfully')
                login(request, user)
                return redirect('profile')
            else:
                messages.warning(request, 'Login information incorrect')
                return redirect('register')
    else:
        form = AuthenticationForm()
    return render(request, 'register.html', {'form': form, 'type': 'Login'})


def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,data=request.POST)
        # form = forms.RegistrstionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form' : form, 'type': 'Password Changing' })

def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(request.POST, instance = request.user)
        # profile_form = forms.RegistrstionForm(request.POST)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('profile')
    else:
        profile_form = forms.ChangeUserForm(instance = request.user)
    return render(request, 'update_profile.html', {'form' : profile_form })



@login_required
def user_logout(request):
    logout(request)
    return redirect('homepage')