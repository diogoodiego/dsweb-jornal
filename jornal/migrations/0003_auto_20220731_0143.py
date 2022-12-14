# Generated by Django 3.2.3 on 2022-07-31 01:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jornal', '0002_edicao'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.CharField(max_length=800)),
                ('data_hora', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=300)),
                ('imagem', models.ImageField(null=True, upload_to='noticias')),
                ('comentarios', models.ManyToManyField(related_name='comentarios', through='jornal.Comentario', to='jornal.Usuario')),
                ('edicao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jornal.edicao')),
            ],
        ),
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jornal.noticia'),
        ),
        migrations.AddField(
            model_name='comentario',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jornal.usuario'),
        ),
    ]
