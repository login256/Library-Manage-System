# Generated by Django 3.0.4 on 2020-03-23 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200323_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookitem',
            name='status',
            field=models.CharField(blank=True, choices=[('Borrowed', 'Borrowed')], default='Not borrowed', max_length=20),
        ),
    ]
