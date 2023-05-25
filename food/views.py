from django.shortcuts import render
from django.views.generic.list import ListView
from .models import Meal
# Create your views here.

class ManageMealListView(ListView):
    # представление, показывающее приемы пищи текущего пользователя
    model = Meal
    template_name = 'food/manage/meal/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)
