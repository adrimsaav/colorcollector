# Generated by Django 4.2.7 on 2023-11-22 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mixing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.color')),
            ],
        ),
    ]