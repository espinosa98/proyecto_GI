# Generated by Django 3.2.6 on 2023-07-28 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=100)),
                ('cantidad', models.IntegerField()),
                ('precio', models.IntegerField()),
                ('categoria', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('fecha_creacion', models.DateField()),
                ('fecha_actualizacion', models.DateField()),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Producto',
        ),
    ]
