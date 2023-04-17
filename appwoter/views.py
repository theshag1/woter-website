from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from appwoter.models import Travel, Category


class CategorylistView(ListView):
    queryset = Category.objects.all()
    template_name = 'base.html'
    context_object_name = 'category'


class Home(ListView):
    queryset = Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'category'


class Enterview(TemplateView):
    template_name = 'enter.html'


class mountain(ListView):
    queryset = Travel.objects.filter(farmname_id=4)
    template_name = 'category/all/mountain.html'
    context_object_name = 'travel'


class sport(ListView):
    template_name = 'category/all/sport.html'
    queryset = Travel.objects.filter(farmname_id=7)
    context_object_name = 'travel'


class asia(ListView):
    template_name = 'category/all/asia.html'
    queryset = Travel.objects.filter(farmname_id=6)
    context_object_name = 'travel'


class europe(ListView):
    template_name = 'category/all/europe.html'
    queryset = Travel.objects.filter(farmname_id=5)
    context_object_name = 'travel'


class river(ListView):
    template_name = 'category/all/rivers.html'
    queryset = Travel.objects.filter(farmname_id=8)
    context_object_name = 'travel'


class Travelview(ListView):
    queryset = Travel.objects.order_by("-id")
    template_name = 'travel/travel.html'
    context_object_name = 'travels'


class Traveldetil(DetailView):
    queryset = Travel.objects.all()
    template_name = 'travel/traveldetil.html'
    context_object_name = 'travel'
