from typing import ItemsView
from django import template
from django.http.response import Http404, HttpResponseServerError
from steplogic.models import *
from django.http import HttpResponse
from django.template import loader


def index(request):

    sites_list = Sites.objects.all().select_related('service_name').order_by('site_name')
    #services_list = Service_name.objects.order_by('id')
    #output = "\n".join([site.site_name for site in sites_list])
    #site_names = [site.site_name for site in sites_list]
    template = loader.get_template('steplogic/index.html')
    context = {
        'sites_list': sites_list,
     #   'services_list': services_list
    }


    return HttpResponse(template.render(context, request))

def detail(request, site_name):
    try:
        #site = Sites.objects.get(site_name=site_name)
        site_count = Sites.objects.filter(site_name=site_name).count()
        if site_count > 1:
            raise HttpResponseServerError("More than one site found. Impossible error!")

        #sites_list = Sites.objects.filter(site_name=site_name).prefetch_related('contacts', 'dependent_service', 'environment')
        #for item in sites_list:
        #    site = item

        site = Sites.objects.get(site_name=site_name)

        environment_list = Env.objects.filter(site=site)

        #for environment in environment_list:
       #     print(environment.get_environment_type_display())

    except Sites.DoesNotExist:
        raise Http404("site does not exists")
    template = loader.get_template('steplogic/detail.html')
    context = {
        'site': site,
        'environment_list': environment_list,
    }
    return HttpResponse(template.render(context, request))

def edit(request, site_name):
    response = "you are editing %s."
    return HttpResponse(response % site_name)

def add(request):
    ###TODO: add functionality for adding site
    pass