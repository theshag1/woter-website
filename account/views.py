from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, TemplateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from .models import CustomUser
from .forms import CustomusercreationForm, Userbuy
from django.contrib.auth.forms import UserChangeForm
from account.forms import CustomUserChangeForm


class UserCHange(UpdateView):
    model = CustomUser
    form_class = CustomUserChangeForm
    template_name = 'registration/change.html'
    success_url = reverse_lazy('home')


class UserBUY(UpdateView):
    model = CustomUser
    form_class = Userbuy
    template_name = 'BUY/buy.html'
    success_url = reverse_lazy('add')


def add(request):
    return render(request, 'add.html')


# Create your views here.

class Signup(CreateView):
    form_class = CustomusercreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
