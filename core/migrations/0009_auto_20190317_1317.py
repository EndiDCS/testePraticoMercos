# Generated by Django 2.1.7 on 2019-03-17 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20190317_1310'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='preco_digitado_pelo_usuario',
            field=models.FloatField(default=550000),
        ),
    ]
