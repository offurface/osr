from django.http import HttpResponse
from django.views.generic import TemplateView

class LandingView(TemplateView):
    template_name = "landing.html"

