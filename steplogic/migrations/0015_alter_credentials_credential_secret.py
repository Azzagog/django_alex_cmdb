# Generated by Django 3.2.7 on 2021-10-12 23:41

from django.db import migrations, models
import django_cryptography.fields


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0014_alter_credentials_credential_secret'),
    ]

    operations = [
        migrations.AlterField(
            model_name='credentials',
            name='credential_secret',
            field=django_cryptography.fields.encrypt(models.CharField(max_length=200)),
        ),
    ]
