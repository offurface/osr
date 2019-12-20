from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.db.models import Max

from .models import (
    Sport_type,
    Coach,
    Parent,
    Sportsman,
    Primary,
    UMO,
    Survey,
)
from .forms import (
    SportTypeForm,
    CoachForm,
    ParentForm,
    SportsmanForm,
    PrimaryForm,
    UMOForm,
)
from django.views.generic import (
    View,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
)


@method_decorator(login_required, name='dispatch')
class RatingListView(View):
    template_name = "registry/rating.html"

    def get(self, request, *args, **kwargs):
        length__max = Survey.objects.aggregate(Max('length'))['length__max']
        weight__max = Survey.objects.aggregate(Max('weight'))['weight__max']
        #foot_length__max = Survey.objects.aggregate(Max('foot_length'))['foot_length__max']
        values = {
            'length__max': length__max,
            'weight__max': weight__max,
            #'foot_length__max': foot_length__max,
        }

        #items = Survey.objects.order_by('sportsman_id','-date' ).values('sportsman_id','date','length','weight')
        items = Survey.objects.order_by('sportsman_id','-date' ).values('sportsman_id','date')
        for i in items:
            print(i)
        #del item[0]
        for i in items:
            print(i)


        return render(request, self.template_name, {
            'length__max': Survey.objects.values()

        })


@method_decorator(login_required, name='dispatch')
class RegitryTemplateView(TemplateView):
    template_name = "registry/registry.html"

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['sporttype'] = Sport_type.objects.all()
        return context
"""
Вид спорта
"""
@method_decorator(login_required, name='dispatch')
class SportTypeListView(ListView):
    template_name = "registry/sport-type/SportType_list.html"
    queryset = Sport_type.objects.all()
    paginate_by = 7
@method_decorator(login_required, name='dispatch')
class SportTypeCreateView(CreateView):
    template_name = "registry/sport-type/SportType_create.html"
    form_class = SportTypeForm
    queryset = Sport_type.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class SportTypeUpdateView(UpdateView):
    template_name = "registry/sport-type/SportType_create.html"
    form_class = SportTypeForm
    queryset = Sport_type.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)
@method_decorator(login_required, name='dispatch')
class SportTypeDetailView(DetailView):
    template_name = "registry/sport-type/SportType_detail.html"
    queryset = Sport_type.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sport_type, pk=pk_)
@method_decorator(login_required, name='dispatch')
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
@method_decorator(login_required, name='dispatch')
class CoachListView(ListView):
    template_name = "registry/coach/coach_list.html"
    queryset = Coach.objects.all()
    paginate_by = 7
@method_decorator(login_required, name='dispatch')
class CoachCreateView(CreateView):
    template_name = "registry/coach/coach_create.html"
    form_class = CoachForm
    queryset = Coach.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class CoachUpdateView(UpdateView):
    template_name = "registry/coach/coach_update.html"
    form_class = CoachForm
    queryset = Coach.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)
@method_decorator(login_required, name='dispatch')
class CoachDetailView(DetailView):
    template_name = "registry/coach/coach_detail.html"
    queryset = Coach.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)
@method_decorator(login_required, name='dispatch')
class CoachDeleteView(DeleteView):
    template_name = "registry/coach/coach_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Coach, pk=pk_)

    def get_success_url(self):
        return reverse("coach-list")


"""
Представители
"""
@method_decorator(login_required, name='dispatch')
class ParentListView(ListView):
    template_name = "registry/parent/parent_list.html"
    queryset = Parent.objects.all()
    paginate_by = 7
@method_decorator(login_required, name='dispatch')
class ParentCreateView(CreateView):
    template_name = "registry/parent/parent_create.html"
    form_class = ParentForm
    queryset = Parent.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)
@method_decorator(login_required, name='dispatch')
class ParentUpdateView(UpdateView):
    template_name = "registry/parent/parent_update.html"
    form_class = ParentForm
    queryset = Parent.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Parent, pk=pk_)
@method_decorator(login_required, name='dispatch')
class ParentDetailView(DetailView):
    template_name = "registry/parent/parent_detail.html"
    queryset = Parent.objects.all()

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Parent, pk=pk_)
@method_decorator(login_required, name='dispatch')
class ParentDeleteView(DeleteView):
    template_name = "registry/parent/parent_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Parent, pk=pk_)

    def get_success_url(self):
        return reverse("parent-list")


"""
Спортсмены
"""
@method_decorator(login_required, name='dispatch')
class SportsmanListView(ListView):
    template_name = "registry/sportsman/sportsman_list.html"
    model = Sportsman
    paginate_by = 20

    def get_queryset(self):
        type_pk = self.request.GET.get('type-pk')
        print(type_pk)
        if type_pk:
            new_queryset = Sportsman.objects.filter(
                sport_type_id=type_pk,
            )
            return new_queryset
        else:
            return Sportsman.objects.all()

@method_decorator(login_required, name='dispatch')
class SportsmanCreateView(CreateView):
    template_name = "registry/sportsman/sportsman_create.html"
    form_class = SportsmanForm
    queryset = Sportsman.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class SportsmanUpdateView(UpdateView):
    template_name = "registry/sportsman/sportsman_update.html"
    form_class = SportsmanForm
    queryset = Sportsman.objects.all()

    def form_valid(self, form):
        return super().form_valid(form)

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sportsman, pk=pk_)

@method_decorator(login_required, name='dispatch')
class SportsmanDetailView(DetailView):
    template_name = "registry/sportsman/sportsman_detail.html"
    queryset = Sportsman.objects.all()

    def get_context_data(self, **kwargs):
        context = super(SportsmanDetailView, self).get_context_data(**kwargs)
        context['primary'] = Primary.objects.filter(sportsman_id=self.object.pk)
        context['umo'] = UMO.objects.filter(sportsman_id=self.object.pk)
        return context

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sportsman, pk=pk_)

@method_decorator(login_required, name='dispatch')
class SportsmanDeleteView(DeleteView):
    template_name = "registry/sportsman/sportsman_delete.html"

    def get_object(self):
        pk_ = self.kwargs.get("pk")
        return get_object_or_404(Sportsman, pk=pk_)

    def get_success_url(self):
        return reverse("sportsman-list")


"""
Первичное обследование
"""
@method_decorator(login_required, name='dispatch')
class PrimaryCreateView(CreateView):
    template_name = "registry/primary/primary_create.html"
    form_class = PrimaryForm
    queryset = Primary.objects.all()
    success_url = '../'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sportsman_id = self.kwargs['pk']
        obj.stage = "Первичный"
        obj.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class UMOCreateView(CreateView):
    template_name = "registry/umo/umo_create.html"
    form_class = UMOForm
    queryset = UMO.objects.all()
    success_url = '../'

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.sportsman_id = self.kwargs['pk']
        obj.save()
        return super().form_valid(form)

# @method_decorator(login_required, name='dispatch')
# class SportsmanUpdateView(UpdateView):
#     template_name = "registry/sportsman/sportsman_update.html"
#     form_class = PrimaryForm
#     queryset = Sportsman.objects.all()

#     def form_valid(self, form):
#         return super().form_valid(form)

#     def get_object(self):
#         pk_ = self.kwargs.get("pk")
#         return get_object_or_404(Sportsman, pk=pk_)

# @method_decorator(login_required, name='dispatch')
# class SportsmanDetailView(DetailView):
#     template_name = "registry/sportsman/sportsman_detail.html"
#     queryset = Sportsman.objects.all()

#     def get_object(self):
#         pk_ = self.kwargs.get("pk")
#         return get_object_or_404(Sportsman, pk=pk_)

# @method_decorator(login_required, name='dispatch')
# class SportsmanDeleteView(DeleteView):
#     template_name = "registry/sportsman/sportsman_delete.html"

#     def get_object(self):
#         pk_ = self.kwargs.get("pk")
#         return get_object_or_404(Sportsman, pk=pk_)

#     def get_success_url(self):
#         return reverse("sportsman-list")
