# Generated by Django 4.2.7 on 2023-12-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_mixing_mix'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mixing',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='mixing',
            name='date',
            field=models.DateField(verbose_name='mixing date'),
        ),
    ]