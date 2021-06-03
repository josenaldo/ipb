from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic

from namelist.models import DevilName


class DevilNameListView(generic.ListView):
    model = DevilName

    # your own name for the list as a template variable
    context_object_name = 'names'

    # Get 5 books containing the title war
    queryset = DevilName.objects.order_by('-creation_date')[:5]

    # Specify your own template name/location
    template_name = 'devil_name_list.html'

    # Override get_context_data() in order to pass additional
    # context variables to the template
    def get_context_data(self, **kwargs):

        # Call the base implementation first to get the context
        context = super(DevilNameListView, self).get_context_data(**kwargs)

        num_names = DevilName.objects.all().count()

        # Create any data and add it to the context
        context['num_names'] = num_names

        return context

# Create your views here.
def index(request):

    num_names = DevilName.objects.all().count()
    last_names = DevilName.objects.order_by('-creation_date')[:5]

    context = {
        'num_names': num_names,
        'last_names': last_names,
    }

    return render(request, 'index.html', context=context)