# Generated by Django 2.1.7 on 2019-03-15 16:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20190307_1738'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='quantidade_digitadada_pelo_usuario',
            new_name='quantidade_digitada_pelo_usuario',
        ),
    ]
