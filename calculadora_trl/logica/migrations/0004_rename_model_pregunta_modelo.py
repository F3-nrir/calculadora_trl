# Generated by Django 4.2.18 on 2025-01-20 02:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('logica', '0003_modelo_tipo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pregunta',
            old_name='model',
            new_name='modelo',
        ),
    ]
