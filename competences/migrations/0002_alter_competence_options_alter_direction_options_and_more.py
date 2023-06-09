# Generated by Django 4.2.1 on 2023-05-27 11:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('competences', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='competence',
            options={'verbose_name': 'Компетенция', 'verbose_name_plural': 'Компетенции'},
        ),
        migrations.AlterModelOptions(
            name='direction',
            options={'verbose_name': 'Направление', 'verbose_name_plural': 'Направления'},
        ),
        migrations.AlterModelOptions(
            name='jobs',
            options={'verbose_name': 'Конкретика', 'verbose_name_plural': 'Конкретики'},
        ),
        migrations.AlterModelOptions(
            name='professions',
            options={'verbose_name': 'Профессиональный стандарт', 'verbose_name_plural': 'Профессиональные стандарты'},
        ),
        migrations.AlterModelOptions(
            name='standards',
            options={'verbose_name': 'Действие', 'verbose_name_plural': 'Действия'},
        ),
        migrations.RemoveField(
            model_name='competence',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='jobs',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='standards',
            name='profession',
        ),
        migrations.AddField(
            model_name='competence',
            name='Профессии',
            field=models.ManyToManyField(to='competences.professions'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Компетенции',
            field=models.ManyToManyField(to='competences.competence'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='Профессии',
            field=models.ManyToManyField(to='competences.professions'),
        ),
        migrations.AddField(
            model_name='jobs',
            name='компетенции (действие)',
            field=models.ManyToManyField(to='competences.standards'),
        ),
        migrations.AddField(
            model_name='standards',
            name='Компетенции',
            field=models.ManyToManyField(to='competences.competence'),
        ),
        migrations.AddField(
            model_name='standards',
            name='Профессии',
            field=models.ManyToManyField(to='competences.professions'),
        ),
        migrations.AlterField(
            model_name='direction',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='professions',
            name='direction',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='competences.direction', verbose_name='Направление'),
        ),
        migrations.AlterField(
            model_name='standards',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Должность с hh.ru'),
        ),
        migrations.CreateModel(
            name='International',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Международные компетенции')),
                ('Профессиональные стандарты', models.ManyToManyField(to='competences.professions')),
            ],
            options={
                'verbose_name': 'Общепрофессиональная компетенция',
                'verbose_name_plural': 'Общепрофессиональные компетенции',
            },
        ),
    ]
