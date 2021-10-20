from typing import Optional
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.expressions import Case

# Create your models here.

class Contacts(models.Model):
    CONTACT_TYPES = models.TextChoices('ContactTtype', "type1 type2 type3" )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    working_hours = models.CharField(max_length=200, blank=True) ### are we sure the working hours will not be changing? with say shifts?
    email = models.EmailField(unique=True) ### this should be our unique identificator
    contact_type = models.CharField(blank=True, choices=CONTACT_TYPES.choices, max_length=200)

    class Meta:
        verbose_name_plural = "Contacts"

    def __str__(self):
        return self.email

class Service_name(models.Model):
    service_name = models.CharField(unique=True, max_length=200)
    service_name_code = models.CharField(max_length=200)
    external_name_description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Service name"

    def __str__(self):
        return self.service_name

class Dependent_services(models.Model):
    service_name = models.CharField(max_length=200)
    service_description = models.CharField(max_length=200)
    external_link = models.URLField()

    class Meta:
        verbose_name_plural = "Dependent services"

    def __str__(self):
        return self.service_name

class Application_patches(models.Model):
    applied_date = models.DateTimeField()
    patch_name = models.CharField(max_length=200)
    patch_description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Application patches"

    def __str__(self):
        return self.patch_name



class Sites(models.Model):
    site_name = models.CharField(max_length=200, unique=True)
    service_name = models.ForeignKey(Service_name, on_delete=CASCADE)
    elr = models.CharField(max_length=200)
    deleted = models.BooleanField()
    working_hours = models.CharField(max_length=200)
    contacts = models.ManyToManyField(Contacts)
    dependent_service = models.ManyToManyField(Dependent_services)
    #environment = models.ForeignKey(Env, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Sites"

    def __str__(self):
        return self.site_name

class Env(models.Model):
    ENVIRONMENT_TYPES = (
        ('TEST', 'TEST'),
        ('PPT', 'PPT'),
        ('PROD', 'Production'),
        ('TRAIN', 'Training'),
    )
    environment_description = models.CharField(max_length=200)
    bigip_url = models.URLField(blank=True)
    url = models.URLField()
    environment_type = models.CharField(max_length=5, choices=ENVIRONMENT_TYPES)
    #credentials = models.ForeignKey(Credentials, on_delete=models.CASCADE)
    #database_info = models.ForeignKey(Database_info, on_delete=models.CASCADE)
    site = models.ForeignKey(Sites, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Environments"

    def __str__(self):
        return self.environment_description

class Application_module(models.Model):
    app_module_code = models.CharField(max_length=200)
    app_module_description = models.CharField(max_length=200)
    app_url = models.CharField(max_length=200)
    app_bigip_url = models.CharField(max_length=200, null=True, blank=True)
    app_port = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Application modules"

    def __str__(self):
        return self.app_module_code

class Application_middleware(models.Model):
    description = models.CharField(max_length=200)
#    application = models.ForeignKey(Application, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Application middleware"

    def __str__(self):
        return self.description

class Application(models.Model):
    application_name = models.CharField(max_length=200)
    application_desc = models.CharField(max_length=200)
    application_patches = models.ManyToManyField(Application_patches)
    middleware_description = models.ForeignKey(Application_middleware, on_delete=CASCADE)
    environment = models.ForeignKey(Env, on_delete=CASCADE)


    class Meta:
        verbose_name_plural = "Applications"

    def __str__(self):
        return self.application_name

class Server_roles(models.Model):
    server_role_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Server_roles"

    def __str__(self):
        return self.server_role_name

class Operative_system_info(models.Model):
    os_name = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Operative_system_info"

    def __str__(self):
        return self.os_name


class Servers(models.Model):
    server_name = models.CharField(max_length=200)
    server_ip = models.CharField(max_length=200)
    server_role_name = models.ForeignKey(Server_roles, on_delete=CASCADE)
    os_version = models.ForeignKey(Operative_system_info, on_delete=CASCADE, null=True, blank=True)
    environment = models.ForeignKey(Env, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Servers"

    def __str__(self):
        return self.server_name



class Credentials(models.Model):
    credential_name = models.CharField(max_length=200)
    credential_secret = models.CharField(max_length=200)
    credential_description = models.CharField(max_length=200)
    environment = models.ForeignKey(Env, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Credentials"

    def __str__(self):
        return self.credential_name

class Database_version(models.Model):
    db_version = models.CharField(max_length=200)  

    class Meta:
        verbose_name_plural = "Databases versions"

    def __str__(self):
        return self.db_version

class Database_info(models.Model):
    cluster_name = models.CharField(max_length=200)
    cluster_ip = models.CharField(max_length=200)
    service_name = models.CharField(max_length=200, null=True, blank=True)
    database_desc = models.CharField(max_length=200)
    user = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    db_version = models.ForeignKey(Database_version, on_delete=CASCADE, null=True, blank=True)
    environment = models.ForeignKey(Env, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Databases info"

    def __str__(self):
        return self.cluster_name