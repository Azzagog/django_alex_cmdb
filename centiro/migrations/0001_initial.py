# Generated by Django 3.2.7 on 2021-10-05 21:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application_middleware',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Application middleware',
            },
        ),
        migrations.CreateModel(
            name='Application_module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_module_code', models.CharField(max_length=200)),
                ('app_module_description', models.CharField(max_length=200)),
                ('app_url', models.CharField(max_length=200)),
                ('app_bigip_url', models.CharField(blank=True, max_length=200, null=True)),
                ('app_port', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Application modules',
            },
        ),
        migrations.CreateModel(
            name='Application_patches',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('applied_date', models.DateTimeField()),
                ('patch_name', models.CharField(max_length=200)),
                ('patch_description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Application patches',
            },
        ),
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('working_hours', models.CharField(blank=True, max_length=200)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('contact_type', models.CharField(blank=True, choices=[('type1', 'Type1'), ('type2', 'Type2'), ('type3', 'Type3')], max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='Dependent_services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200)),
                ('service_description', models.CharField(max_length=200)),
                ('external_link', models.URLField()),
            ],
            options={
                'verbose_name_plural': 'Dependent services',
            },
        ),
        migrations.CreateModel(
            name='Env',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('environment_description', models.CharField(max_length=200)),
                ('bigip_url', models.URLField(blank=True)),
                ('url', models.URLField()),
                ('environment_type', models.CharField(choices=[('TEST', 'TEST'), ('PPT', 'PPT'), ('PROD', 'Production'), ('TRAIN', 'Training')], max_length=5)),
            ],
            options={
                'verbose_name_plural': 'Environments',
            },
        ),
        migrations.CreateModel(
            name='Service_name',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=200, unique=True)),
                ('service_name_code', models.CharField(max_length=200)),
                ('external_name_description', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Service name',
            },
        ),
        migrations.CreateModel(
            name='Sites',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=200, unique=True)),
                ('elr', models.CharField(max_length=200)),
                ('deleted', models.BooleanField()),
                ('working_hours', models.CharField(max_length=200)),
                ('contacts', models.ManyToManyField(to='centiro.Contacts')),
                ('dependent_service', models.ManyToManyField(to='centiro.Dependent_services')),
                ('service_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.service_name')),
            ],
            options={
                'verbose_name_plural': 'Sites',
            },
        ),
        migrations.CreateModel(
            name='Servers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('server_name', models.CharField(max_length=200)),
                ('server_ip', models.CharField(max_length=200)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.env')),
            ],
            options={
                'verbose_name_plural': 'Servers',
            },
        ),
        migrations.AddField(
            model_name='env',
            name='site',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.sites'),
        ),
        migrations.CreateModel(
            name='Database_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cluster_name', models.CharField(max_length=200)),
                ('cluster_ip', models.CharField(max_length=200)),
                ('database_desc', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.env')),
            ],
            options={
                'verbose_name_plural': 'Databases info',
            },
        ),
        migrations.CreateModel(
            name='Credentials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('credential_name', models.CharField(max_length=200)),
                ('credential_secret', models.CharField(max_length=200)),
                ('credential_description', models.CharField(max_length=200)),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.env')),
            ],
            options={
                'verbose_name_plural': 'Credentials',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_name', models.CharField(max_length=200)),
                ('application_desc', models.CharField(max_length=200)),
                ('application_patches', models.ManyToManyField(to='centiro.Application_patches')),
                ('environment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.env')),
                ('middleware_description', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centiro.application_middleware')),
            ],
            options={
                'verbose_name_plural': 'Applications',
            },
        ),
    ]
