# Generated by Django 2.2.7 on 2019-11-28 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='')),
                ('apellidos', models.TextField(verbose_name='')),
                ('fecha_nacimiento', models.DateField(verbose_name='')),
                ('parentesco', models.TextField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Informe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_informe', models.DateField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Residente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.TextField(verbose_name='')),
                ('apellidos', models.TextField(verbose_name='')),
                ('fecha_nacimiento', models.DateField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ParteInforme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(choices=[('S', 'SANITARIA'), ('F', 'FUNCIONAL'), ('P', 'PSIQUICA'), ('S', 'SOCIAL'), ('TO', 'TERAPIA OCUPACIONAL')], max_length=2)),
                ('valoracion_inicial', models.IntegerField(verbose_name='')),
                ('objetivos', models.TextField(verbose_name='')),
                ('informe', models.ManyToManyField(to='programaindividualizado.Informe', verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='informe',
            name='partes',
            field=models.ManyToManyField(related_name='Partes', to='programaindividualizado.ParteInforme', verbose_name=''),
        ),
    ]
