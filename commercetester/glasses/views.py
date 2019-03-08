from django.shortcuts import render
from django.views import generic
from .models import Site, Supposition
class IndexView(generic.ListView):
    template_name = 'glasses/index.html'
    context_object_name = 'site_list'
    fields = ['url']
    model = Site

    def get_queryset(self):
        return Site.objects.order_by('-pubdate')
