from typing import ItemsView
from django import template
from django.http.response import Http404, HttpResponseServerError
from steplogic.models import *
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


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

def login_view(request):
    sites_list2 = Sites.objects.all().select_related('service_name').order_by('site_name')
    template2 = loader.get_template('steplogic/login_view.html')    
    context2 = {
        'sites_list': sites_list2,
     #   'services_list': services_list
    }     
    return HttpResponse(template2.render(context2, request))

def detail(request, site_name):
    site = get_object_or_404(Sites, site_name=site_name)
    return render(request, 'steplogic/sites.html', {'site' : site})

def contacts(request, site_name):
    site = get_object_or_404(Sites, site_name=site_name)
    return render(request, 'steplogic/contacts.html', {'site' : site})

#def environment(request, site_name):
#    site = get_object_or_404(Sites, site_name=site_name)
#    return render(request, 'steplogic/environment.html', {'site' : site})

def dependent_service(request, site_name):
    site = get_object_or_404(Sites, site_name=site_name)
    return render(request, 'steplogic/dependent_service.html', {'site' : site})

def environments(request):    
    environments_list = Env.objects.all()
    template = loader.get_template('steplogic/environment.html')
    context = {
        'environments_list': environments_list,     
    }

    return HttpResponse(template.render(context, request))
def applications_detail(request,site_name, environment_description , application_name):
    #err
    template = loader.get_template('steplogic/application_detail.html')
    site = Sites.objects.get(site_name=site_name)
    environment = Env.objects.get(environment_description=environment_description)
    application = Application.objects.get(application_name=application_name)    
    application_modules_list = Application_module.objects.filter(application=application)
    patches_list=Application_patches.objects.filter(application=application)    
    print(type(environment))
    print(type(application))
    context= {
        'site': site,
        'environment' : environment,
        'application' : application,
        'application_modules_list' : application_modules_list,
        'patches_list' : patches_list,
    }

    return HttpResponse(template.render(context,request))

def environment_detail(request,site_name, environment_description):
    #err
    template = loader.get_template('steplogic/environment_detail.html')
    site = Sites.objects.get(site_name=site_name)
    environment = Env.objects.get(environment_description=environment_description)
    credentials_list = Credentials.objects.filter(environment=environment)
    database_list = Database_info.objects.filter(environment=environment)
    server_list = Servers.objects.filter(environment=environment)
    application_list = Application.objects.filter(environment=environment)    
    print(type(environment))
    context= {
        'site': site,
        'environment' : environment,
        'credentials_list' : credentials_list,
        'database_list' : database_list,
        'server_list' : server_list,
        'application_list' : application_list,
    }

    return HttpResponse(template.render(context,request))

def edit(request, site_name):
    response = "you are editing %s."
    return HttpResponse(response % site_name)

def add(request):
    ###TODO: add functionality for adding site
    pass