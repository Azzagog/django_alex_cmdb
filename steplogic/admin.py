from django.contrib import admin

# Register your models here.

#from .models import Contacts
#from .models import Sites
from .models import *

admin.site.register(Contacts)
admin.site.register(Sites)
admin.site.register(Service_name)
admin.site.register(Dependent_services)
admin.site.register(Application_patches)
admin.site.register(Application_middleware)
admin.site.register(Application_module)
admin.site.register(Application)
admin.site.register(Servers)
admin.site.register(Database_info)
admin.site.register(Credentials)
admin.site.register(Env)
admin.site.register(Server_roles)
admin.site.register(Operative_system_info)
admin.site.register(Database_version)
