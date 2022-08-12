# Generated by Django 3.2.3 on 2022-08-01 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0003_auto_20220731_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='edicao',
            name='data_fim',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='edicao',
            name='data_inicio',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='comentarios',
            field=models.ManyToManyField(related_name='comentarios', through='jornal.Comentario', to='jornal.Usuario'),
        ),
    ]
