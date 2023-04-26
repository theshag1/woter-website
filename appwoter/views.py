from django.http import Http404
from django.shortcuts import render
from django.views.generic import ListView, TemplateView, DetailView
from appwoter.models import Travel, Category


class CategoryListview(ListView):
    queryset = Category.objects.all()
    template_name = 'base.html'
    context_object_name = 'categorys'


class CategoryView(DetailView):
    queryset = Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'categorys'


class Home(ListView):
    queryset = Category.objects.all()
    template_name = 'home.html'
    context_object_name = 'category'


class Enterview(TemplateView):
    template_name = 'enter.html'


def Categorys(request, pk):
    context = {
        'travel': Travel.objects.get(farmname_id=pk)
    }

    return render(request, 'category/all.html', context=context)




class Travelview(ListView):
    queryset = Travel.objects.order_by("-id")
    template_name = 'travel/travel.html'
    context_object_name = 'travels'


class Traveldetil(DetailView):
    queryset = Travel.objects.all()
    template_name = 'travel/traveldetil.html'
    context_object_name = 'travel'
