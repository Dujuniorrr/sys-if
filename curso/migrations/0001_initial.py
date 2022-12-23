# Generated by Django 4.1.3 on 2022-11-12 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_curso', models.CharField(max_length=250, verbose_name='Nome')),
                ('codigo_curso', models.CharField(max_length=100, verbose_name='Código curso')),
                ('descricao', models.CharField(max_length=500, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Curso',
                'ordering': ['nome_curso'],
            },
        ),
    ]