# Generated by Django 3.2.8 on 2021-10-20 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('steplogic', '0016_auto_20211020_0503'),
    ]

    operations = [
        migrations.AddField(
            model_name='database_info',
            name='service_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
