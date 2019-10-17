from django.shortcuts import render

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
)
class SportTypeView(ListView):
    template_name = "registry/sport-type/SportType_list.html"
    queryset = Sport_type.objects.all()
    #context_object_name
    paginate_by = 7

class SportTypeCreateView(CreateView):
    template_name = "registry/sport-type/SportType_create.html"
    form_class = SportTypeForm
    queryset = Sport_type.objects.all()

class SportTypeDetailView(DetailView):
    template_name = "registry/sport-type/SportType_detail.html"
    queryset = Sport_type.objects.all()
