from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from namelist.models import DevilName
from namelist.forms import NewDevilNameForm
from namelist.serializers import DevilNameSerializer

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

@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def random_name(request):
    devilname = DevilName.randoms.random()
    serializer = DevilNameSerializer(devilname)
    return Response(serializer.data)

def nomes(request):
    context = {

    }

    return render(request, 'invocacao.html', context=context)

class DevilNameViewSet(viewsets.ModelViewSet):
    queryset = DevilName.objects.all()
    serializer_class = DevilNameSerializer

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
    success_url = reverse_lazy('devilname_list')

class DevilNameList(ListView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name ='devilname_list'

    # Get 5 books containing the title war
    queryset = DevilName.objects.order_by('id')

    # Especifica a localização do template, a partir da pasta templates
    # template_name = 'devilname_list.html'

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
    context_object_name ='devilname'


# @permission_required('namelist.add_devilname', raise_exception=True)
# def devilname_add(request):

#     context = {}

#     if(request.method == 'POST'):
#         form = NewDevilNameForm(request.POST)

#         if form.is_valid():

#             existent_devilname = DevilName.objects.filter(name=form.cleaned_data['name'])

#             if(existent_devilname):
#                 message = "Nome do capeta já existe."
#             else:
#                 devilname_instance = DevilName()
#                 devilname_instance.name = form.cleaned_data['name']
#                 devilname_instance.save()

#                 message = "Nome do capeta adicionado: " + devilname_instance.name
#                 form = NewDevilNameForm()

#             context['message'] = message

#     else:
#         form = NewDevilNameForm()

#     context['form'] = form

#     return render(request, 'devilname_add.html', context)