# Generated by Django 4.2.2 on 2023-06-30 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='published_at',
            field=models.DateField(auto_now=True),
        ),
    ]
