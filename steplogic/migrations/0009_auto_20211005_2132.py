# Generated by Django 3.2.7 on 2021-10-05 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0008_alter_application_module_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application_module',
            name='application_id',
        ),
        migrations.RemoveField(
            model_name='application',
            name='application_patches',
        ),
        migrations.AddField(
            model_name='application',
            name='application_patches',
            field=models.ManyToManyField(to='steplogic.Application_patches'),
        ),
        migrations.AlterField(
            model_name='application_module',
            name='app_bigip_url',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
