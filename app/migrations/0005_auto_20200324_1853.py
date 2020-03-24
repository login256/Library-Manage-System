# Generated by Django 3.0.4 on 2020-03-24 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20200323_2024'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookitem',
            name='status',
            field=models.IntegerField(choices=[(0, '未借出'), (1, '已借出')], default=0),
        ),
    ]
