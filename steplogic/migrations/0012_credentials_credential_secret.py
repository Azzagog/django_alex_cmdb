# Generated by Django 3.2.7 on 2021-10-12 23:14

from django.db import migrations, models
import django_cryptography.fields
from steplogic.models import Credentials

class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0011_rename_credential_secret_credentials_old_credential_secret'),
    ]

    operations = [
        migrations.AddField(
            model_name='credentials',
            name='credential_secret',
            field=django_cryptography.fields.encrypt(models.CharField(default="", max_length=200)),
        ),
    ]
