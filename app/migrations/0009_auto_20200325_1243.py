# Generated by Django 3.0.4 on 2020-03-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20200325_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='student_number',
            field=models.CharField(max_length=20, null=True, verbose_name='学号'),
        ),
    ]
