# Generated by Django 3.1.4 on 2020-12-20 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_auto_20201220_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='next_visit_date',
            field=models.CharField(max_length=150),
        ),
    ]
