# Generated by Django 3.2.8 on 2021-10-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0025_credentials_credential_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='application_version',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
