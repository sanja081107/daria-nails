# Generated by Django 4.0.7 on 2022-09-23 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_customuser_options_alter_myworks_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myworks',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Дата'),
        ),
    ]