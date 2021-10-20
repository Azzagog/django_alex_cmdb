from django.contrib import admin

from django.apps import apps


# Register your models here.

#from .models import Contacts
#from .models import Sites
from .models import *

models = apps.get_app_config('steplogic').get_models()


for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

# admin.site.register(Contacts)
# admin.site.register(Sites)
# admin.site.register(Service_name)
# admin.site.register(Dependent_services)
# admin.site.register(Application_patches)
# admin.site.register(Application_middleware)
# admin.site.register(Application_module)
# admin.site.register(Application)
# admin.site.register(Servers)
# admin.site.register(Database_info)
# admin.site.register(Credentials)
# admin.site.register(Env)
