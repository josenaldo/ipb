from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from namelist.models import DevilName
from namelist.forms import NewDevilNameForm

# Create your views here.
def index(request):

    context = {

    }

    return render(request, 'index.html', context=context)

def invocacao(request):

    context = {
        'my_data_main': 'app-invocacao.js'
    }

    return render(request, 'invocacao.html', context=context)

def nomes(request):
    context = {

    }

    return render(request, 'invocacao.html', context=context)

# @permission_required('namelist.add_devilname', raise_exception=True)
class DevilNameCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'namelist.add_devilname'
    model = DevilName
    fields = ['name']

class DevilNameUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'namelist.change_devilname'
    model = DevilName
    fields = ['name']

class DevilNameDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'namelist.delete_devilname'
    model = DevilName
    success_url = reverse_lazy('devil_name_list')

class DevilNameList(ListView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name ='devil_name_list'

    # Get 5 books containing the title war
    #queryset = DevilName.objects.order_by('-creation_date')[:5]

    # Especifica a localização do template, a partir da pasta templates
    # template_name = 'devil_name_list.html'

    # especifica o número máximo de itens que deve aparecer na lista
    paginate_by = 10

    # Override get_context_data() in order to pass additional
    # context variables to the template
    def get_context_data(self, **kwargs):

        # MANDATORY!
        # First get the existing context from our superclass.        
        context = super(DevilNameList, self).get_context_data(**kwargs)

        # Then add your new context information.
        num_names = DevilName.objects.all().count()
        context['num_names'] = num_names

        # MANDATORY!
        # Then return the new (updated) context.
        return context

class DevilNameDetail(DetailView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name ='devil_name'

    # Specify your own template name/location
    # template_name = 'devil_name_detail.html'


# @permission_required('namelist.add_devilname', raise_exception=True)
# def devil_name_add(request):

#     context = {}

#     if(request.method == 'POST'):
#         form = NewDevilNameForm(request.POST)

#         if form.is_valid():

#             existent_devil_name = DevilName.objects.filter(name=form.cleaned_data['name'])

#             if(existent_devil_name):
#                 message = "Nome do capeta já existe."
#             else:
#                 devil_name_instance = DevilName()
#                 devil_name_instance.name = form.cleaned_data['name']
#                 devil_name_instance.save()

#                 message = "Nome do capeta adicionado: " + devil_name_instance.name
#                 form = NewDevilNameForm()

#             context['message'] = message

#     else:
#         form = NewDevilNameForm()

#     context['form'] = form

#     return render(request, 'devil_name_add.html', context)