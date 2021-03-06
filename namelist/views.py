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
from namelist.forms import DevilNameSearchForm, ImportDevilNameForm
from namelist.serializers import DevilNameSerializer

# Create your views here.


def index(request):

    context = {
        'my_data_main': 'app-main.js',
        'page_title': 'Invoca Piroto',
    }

    count_names = DevilName.objects.all().count()
    context['count'] = count_names

    devilname_list = DevilName.objects.all().order_by('-id')[:5]
    context['devilname_list'] = devilname_list

    return render(request, 'index.html', context=context)


def invocacao(request):

    context = {
        'my_data_main': 'app-invocacao.js',
        'page_title': 'Invoca Piroto',
    }

    return render(request, 'invocacao.html', context=context)


def forca(request):

    context = {
        'my_data_main': 'app-forca.js',
        'page_title': 'Enforca Piroto',
    }

    return render(request, 'forca.html', context=context)

from django.forms.models import modelform_factory

@permission_required('namelist.add_devilname')
def devilname_import(request):
    context = {
        'page_title': 'Importar Nomes do Capeta',
    }

    if request.method == "POST":

        form = ImportDevilNameForm(request.POST, request.FILES)

        if form.is_valid():

            csv_file = request.FILES['csv_file']

            # let's check if it is a csv file
            if not csv_file.name.endswith('.csv'):
                messages.error(request, 'THIS IS NOT A CSV FILE')

            data_set = csv_file.read().decode('UTF-8')

            io_string = io.StringIO(data_set)

            fail_names = []

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
                messages.warning(
                    request, f'Nomes n??o importados: {len(fail_names)}')
                context['fail_names'] = fail_names
    else:
        form = ImportDevilNameForm()

    context['form'] = form

    return render(request, 'namelist/devilname_import.html', context=context)


class DevilNameCreate(PermissionRequiredMixin, CreateView):

    permission_required = 'namelist.add_devilname'
    model = DevilName
    form_class = modelform_factory(DevilName, fields=(('name',)), error_messages={'name':{'required': 'Vai invocar um capiroto sem nome, mizera?'}})

    def get_context_data(self, **kwargs):

        context = super(DevilNameCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Registrar Nome do Capeta'
        return context


class DevilNameUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'namelist.change_devilname'
    model = DevilName
    form_class = modelform_factory(DevilName, fields=(('name',)), error_messages={'name':{'required': 'Vai invocar um capiroto sem nome, mizera?'}})

    def get_context_data(self, **kwargs):

        context = super(DevilNameUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Atualizar Nome do Capeta'
        return context


class DevilNameDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'namelist.delete_devilname'
    model = DevilName
    success_url = reverse_lazy('devilname_list')

    def get_context_data(self, **kwargs):

        context = super(DevilNameDelete, self).get_context_data(**kwargs)
        context['page_title'] = 'Deletar Nome do Capeta'
        return context


class DevilNameList(ListView):
    model = DevilName
    context_object_name = 'devilname_list'
    ordering = 'id'
    paginate_by = 10
    form_class = DevilNameSearchForm

    def get_context_data(self, **kwargs):

        context = super(DevilNameList, self).get_context_data(**kwargs)

        form = self.form_class(self.request.GET)
        context['form'] = form

        num_names = DevilName.objects.all().count()
        context['count'] = num_names
        context['page_title'] = 'Lista de Nomes do Capeta'
        context['ordering'] = self.get_ordering()

        return context

    def get_queryset(self):

        form = self.form_class(self.request.GET)

        if form.is_valid():
            search = form.cleaned_data['search']

            if search:
                return self.model.objects.filter(name__icontains=search).order_by(self.get_ordering())

        return self.model.objects.all().order_by(self.get_ordering())

    def get_ordering(self):
        ordering_param = self.request.GET.get('ordering', '')

        if ordering_param:
            ordering = ordering_param
        else:
            ordering = 'id'

        return ordering


class DevilNameDetail(DetailView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name = 'devilname'

    def get_context_data(self, **kwargs):

        context = super(DevilNameDetail, self).get_context_data(**kwargs)
        context['page_title'] = 'Detalhes do Nome do Capeta'
        return context


@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def random_name(request):
    """ Retorna um nome do capeta aleat??rio """

    devilname = DevilName.randoms.random()
    serializer = DevilNameSerializer(devilname)
    return Response(serializer.data)


@permission_classes((permissions.AllowAny,))
class DevilNameViewSet(viewsets.ModelViewSet):
    """ Implementa API de nomes do capeta """

    queryset = DevilName.objects.all()
    serializer_class = DevilNameSerializer
