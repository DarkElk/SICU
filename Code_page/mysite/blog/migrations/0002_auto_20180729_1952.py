# Generated by Django 2.0.6 on 2018-07-29 23:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios_registrados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('correo', models.CharField(max_length=100)),
                ('contraseña', models.CharField(max_length=100)),
                ('carrera', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='titulo',
            field=models.CharField(max_length=100),
        ),
    ]