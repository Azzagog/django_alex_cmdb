# Generated by Django 3.2.8 on 2021-10-25 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0022_auto_20211025_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='application_modules',
            field=models.ManyToManyField(to='steplogic.Application_module'),
        ),
        migrations.AlterField(
            model_name='application',
            name='application_patches',
            field=models.ManyToManyField(to='steplogic.Application_patches'),
        ),
    ]
