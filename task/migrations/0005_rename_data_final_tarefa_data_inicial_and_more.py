# Generated by Django 5.0.6 on 2024-06-11 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0004_remove_tarefa_cliente'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarefa',
            old_name='data_final',
            new_name='data_inicial',
        ),
        migrations.AlterField(
            model_name='tarefa',
            name='data_base',
            field=models.DateField(auto_now_add=True),
        ),
    ]