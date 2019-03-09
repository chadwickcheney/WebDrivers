from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Site, Supposition
from .forms import PilotForm
import datetime

class IndexView(generic.ListView):
    template_name = 'glasses/index.html'
    context_object_name = 'site_list'
    fields = ['url']
    form_class = PilotForm
    model = Site

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['site_list'] = Site.objects.all()
        context.update({'form':self.form_class})
        return context

    def post(self, request):
        if request.method == 'POST':
            site=''
            url=''
            form = PilotForm(request.POST)
            if form.is_valid():
                url,url_test = self.validate_url(request.POST.get('url'))
            try: #fails = site is new and requires a report
                site = Site.objects.get(url__contains=url)
            except Site.DoesNotExist:
                site = Site(url=url,pub_date=datetime.datetime.now())
                site.save()

        return HttpResponseRedirect(reverse('glasses:detail', args=(site.id,)))

    def get_queryset(self):
        return Site.objects.order_by('-pubdate')

    def validate_url(self, url):
        import re
        regex = re.compile(
            r'^(?:http|ftp)s?://' # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
            r'localhost|' #localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
            r'(?::\d+)?' # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE
        )
        return url,re.match(regex, url) is not None

class DetailView(generic.DetailView):
    model = Site
    template_name = 'glasses/detail.html'
    context_object_name = 'supposition_list'
    fields = ['response']
    form_class = PilotForm.ResponseForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        supposition = None
        site=Site.objects.get(url__contains=kwargs['object'])
        try:
            supposition = Supposition.objects.get(site=site)
            context['supposition_list'] = supposition
        except:
            context['supposition_list'] = None

        context.update({'form':self.form_class})
        return context
