# Generated by Django 4.2.1 on 2023-05-18 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Direction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Направление')),
            ],
        ),
        migrations.CreateModel(
            name='Professions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Профессия')),
                ('direction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competences.direction')),
            ],
        ),
        migrations.CreateModel(
            name='Standards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Стандарт')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competences.professions')),
            ],
        ),
        migrations.CreateModel(
            name='Jobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Конкретика')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competences.professions')),
            ],
        ),
        migrations.CreateModel(
            name='Competence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Компетенция')),
                ('profession', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competences.professions')),
            ],
        ),
    ]