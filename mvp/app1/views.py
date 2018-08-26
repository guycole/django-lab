from django.shortcuts import render

# Create your views here.

from django import forms

from django.http import HttpResponse

from django.views import generic
from django.views.generic.edit import CreateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import UpdateView

from django.urls import reverse_lazy

from .models import Alpha

def ok(request):
    return HttpResponse("ok")

class IndexView(generic.ListView):
    template_name = 'app1/index.html'
    context_object_name = 'alpha_result_list'

    def get_queryset(self):
        return Alpha.objects.order_by('int_val')

class AlphaForm(forms.ModelForm):
    class Meta:
        model = Alpha
        fields = ['int_val', 'string_val']
#       labels = {'int_val': _('integer'), 'string_val': _('string')}
#       help_texts = {'int_val': _('int help'), 'string_val': _('string help')}

class AlphaDetailView(generic.DetailView):
    model = Alpha
    template_name = 'app1/alpha_detail.html'

class AlphaCreate(CreateView):
    model = Alpha
    fields = '__all__'
    labels = {'int_val': 'integer', 'string_val': 'string'}
    initial = {'int_val': 12345, 'string_val': 'bogus'}

class AlphaDelete(DeleteView):
    model = Alpha
    success_url = reverse_lazy('app1:ok')

class AlphaUpdate(UpdateView):
    model = Alpha
    fields = ['int_val', 'string_val']