# Generated by Django 3.2.7 on 2021-10-01 20:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0006_auto_20211001_2016'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name_plural': 'Applications'},
        ),
        migrations.AlterModelOptions(
            name='application_middleware',
            options={'verbose_name_plural': 'Application middleware'},
        ),
        migrations.AlterModelOptions(
            name='application_module',
            options={'verbose_name_plural': 'Application_modules'},
        ),
        migrations.AlterModelOptions(
            name='application_patches',
            options={'verbose_name_plural': 'Application patches'},
        ),
        migrations.AlterModelOptions(
            name='credentials',
            options={'verbose_name_plural': 'Credentials'},
        ),
        migrations.AlterModelOptions(
            name='database_info',
            options={'verbose_name_plural': 'Databases info'},
        ),
        migrations.AlterModelOptions(
            name='dependent_services',
            options={'verbose_name_plural': 'Dependent services'},
        ),
        migrations.AlterModelOptions(
            name='env',
            options={'verbose_name_plural': 'Environments'},
        ),
        migrations.AlterModelOptions(
            name='servers',
            options={'verbose_name_plural': 'Servers'},
        ),
        migrations.AlterModelOptions(
            name='service_name',
            options={'verbose_name_plural': 'Service name'},
        ),
    ]
