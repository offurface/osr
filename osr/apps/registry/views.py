from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import (
    Sport_type,
)
from .forms import (
    SportTypeForm,
)
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

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
        id_ = self.kwargs.get("id")
        return get_object_or_404(Sport_type, id_)

class SportTypeDetailView(DetailView):
    template_name = "registry/sport-type/SportType_detail.html"
    queryset = Sport_type.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)

class SportTypeDeleteView(DeleteView):
    template_name = "registry/sport-type/SportType_delete.html"

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Sport_type, id_)

    def get_success_url(self):
        return reverse("sport-type-list")


