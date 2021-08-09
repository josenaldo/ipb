from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib import messages
from django.db import IntegrityError

import csv
import io
from datetime import datetime

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions

from namelist.models import DevilName
from namelist.forms import ImportDevilNameForm
from namelist.serializers import DevilNameSerializer

# Create your views here.


def index(request):

    context = {}

    return render(request, 'index.html', context=context)


def invocacao(request):

    context = {
        'my_data_main': 'app-invocacao.js'
    }

    return render(request, 'invocacao.html', context=context)

def forca(request):

    context = {
        'my_data_main': 'app-forca.js'
    }

    return render(request, 'forca.html', context=context)

@permission_required('namelist.add_devilname')
def devilname_import(request):
    context = {}

    if request.method == "POST":

        form = ImportDevilNameForm(request.POST, request.FILES)

        if form.is_valid():

            csv_file = request.FILES['csv_file']

            # let's check if it is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')

            data_set = csv_file.read().decode('UTF-8')

            io_string = io.StringIO(data_set)

            fail_names=[]

            next(io_string)
            for column in csv.reader(io_string, delimiter=',', quotechar="\""):

                try:
                    _, created = DevilName.objects.update_or_create(
                        name=column[0],
                        creation_date=datetime.strptime(
                            column[1], '%d/%m/%Y %H:%M:%S'),
                    )

                except IntegrityError as saveException:
                    fail_names.append(column[0])


            messages.success(request, 'Arquivo importado com sucesso')

            if(len(fail_names) > 0):
                messages.warning(request, f'Nomes não importados: {len(fail_names)}')
                context['fail_names'] = fail_names
    else:
        form = ImportDevilNameForm()

    context['form'] = form

    return render(request, 'namelist/devilname_import.html', context=context)


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def random_name(request):
    devilname = DevilName.randoms.random()
    serializer = DevilNameSerializer(devilname)
    return Response(serializer.data)


def nomes(request):
    context = {

    }

    return render(request, 'namelist/invocacao.html', context=context)


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
    context_object_name = 'devilname_list'

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
        context['count'] = num_names

        # MANDATORY!
        # Then return the new (updated) context.
        return context

    def get_ordering(self):
        ordering = self.request.GET.get('ordering', '-id')
        # validate ordering here
        return ordering


class DevilNameDetail(DetailView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name = 'devilname'


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
