# Generated by Django 2.1.7 on 2019-04-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190408_2131'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='charclass',
            field=models.CharField(choices=[('Mago', 'Mago'), ('Cavaleiro', 'Cavaleiro'), ('Druida', 'Druida'), ('Clérigo', 'Clérigo'), ('Feiticeiro', 'Feiticeiro'), ('Atirador', 'Atirador'), ('Ladino', 'Ladino'), ('Monge', 'Monge')], default='Cavaleiro', max_length=10),
        ),
    ]
