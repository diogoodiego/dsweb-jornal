# Generated by Django 3.2.3 on 2022-08-01 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0006_auto_20220801_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='comentarios',
            field=models.ManyToManyField(related_name='comentarios', through='jornal.Comentario', to='jornal.Usuario'),
        ),
    ]
