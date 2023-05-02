# Generated by Django 4.2 on 2023-04-30 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_categoria_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categoria',
            name='nombre',
            field=models.IntegerField(choices=[(1, 'Tecnología'), (2, 'Ciencia'), (3, 'Arte y cultura'), (4, 'Historia'), (5, 'Política'), (6, 'Economía'), (7, 'Deportes'), (8, 'Salud y bienestar'), (9, 'Medio ambiente'), (10, 'Educación'), (11, 'Matemáticas'), (12, 'Cocina'), (13, 'Psicología')]),
        ),
    ]
