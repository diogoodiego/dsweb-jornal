# Generated by Django 3.2.14 on 2022-08-14 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0012_auto_20220811_0244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='comentarios',
            field=models.ManyToManyField(related_name='comentarios', through='jornal.Comentario', to='jornal.Usuario'),
        ),
    ]
