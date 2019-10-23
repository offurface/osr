from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import (
    Sport_type,
    Coach,
    Parent,
    Sportsman,
)
from .forms import (
    SportTypeForm,
    CoachForm,
    ParentForm,
    SportsmanForm,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)

class RegitryTemplateView(TemplateView):
    template_name = "registry/registry.html"

"""
Вид спорта
"""
class SportTypeListView(ListView):
    template_name = "registry/sport-type/SportType_list.html"
    queryset = Sport_type.objects.all()
    paginate_by = 7

class SportTypeCreateView(CreateView):
    template_name = "registry/sport-type/SportType_create.html"
    form_class = SportTypeForm
    queryset = Sport_type.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class SportTypeUpdateView(UpdateView):
    template_name = "registry/sport-type/SportType_create.html"
    form_class = SportTypeForm
    queryset = Sport_type.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)

class SportTypeDetailView(DetailView):
    template_name = "registry/sport-type/SportType_detail.html"
    queryset = Sport_type.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)

class SportTypeDeleteView(DeleteView):
    template_name = "registry/sport-type/SportType_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)

    def get_success_url(self):
        return reverse("sport-type-list")
"""
ТРЕНЕРА
"""
class CoachListView(ListView):
    template_name = "registry/coach/coach_list.html"
    queryset = Coach.objects.all()
    paginate_by = 7

class CoachCreateView(CreateView):
    template_name = "registry/coach/coach_create.html"
    form_class = CoachForm
    queryset = Coach.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

class CoachUpdateView(UpdateView):
    template_name = "registry/coach/coach_update.html"
    form_class = CoachForm
    queryset = Coach.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)

class CoachDetailView(DetailView):
    template_name = "registry/coach/coach_detail.html"
    queryset = Coach.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)

class CoachDeleteView(DeleteView):
    template_name = "registry/coach/coach_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)

    def get_success_url(self):
        return reverse("coach-list")
