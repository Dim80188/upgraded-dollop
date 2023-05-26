from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from .models import Meal
# Create your views here.


class OwnerMixin:
    # миксин, определяющий принадлежность
    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(owner=self.request.user)

class OwnerEditMixin:
    # утанавливает текущего пользователя в атрибуте owner сохраняемого объекта
    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class OwnerMealMixin(OwnerMixin, LoginRequiredMixin, PermissionRequiredMixin):
    # передает указанные ниже атрибуты для представлений CreateView, UpdateView
    model = Meal
    fields = ['title', 'description', 'event_time']
    success_url = reverse_lazy('manage_course_list')

class OwnerMealEditMixin(OwnerMealMixin, OwnerEditMixin):
    # определяет шаблон, который будет использоваться для CreateView, UpdateView
    template_name = 'food/manage/meal/form.html'


class ManageMealListView(OwnerMealMixin, ListView):
    # представление, показывающее приемы пищи текущего пользователя
    template_name = 'food/manage/meal/list.html'

class MealCreateView(OwnerCourseEditMixin, CreateView):
    pass

class MealUpdateView(OwnerMealEditMixin, UpdateView):
    pass

class MealDeleteView(OwnerMealMixin, DeleteView):
    template_name = 'food/manage/meal/delete.html'
