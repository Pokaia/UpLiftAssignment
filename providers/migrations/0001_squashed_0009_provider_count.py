# Generated by Django 3.2.19 on 2023-05-23 19:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [('providers', '0001_initial'), ('providers', '0002_auto_20230520_0123'), ('providers', '0003_auto_20230520_1801'), ('providers', '0004_rename_providerskills_providerskill'), ('providers', '0005_auto_20230522_2034'), ('providers', '0006_rename_languange_provider_language'), ('providers', '0007_provider_skills'), ('providers', '0008_remove_provider_skills'), ('providers', '0009_provider_count')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=100)),
                ('birth_date', models.DateField()),
                ('rating', models.DecimalField(decimal_places=1, max_digits=4)),
                ('company', models.CharField(max_length=100)),
                ('active', models.BooleanField()),
                ('country', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ProviderSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(0, 'primary'), (1, 'secondary')], default=0)),
                ('provider', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.provider')),
                ('skill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='providers.skill')),
            ],
            options={
                'unique_together': {('provider', 'skill', 'type')},
            },
        ),
    ]
