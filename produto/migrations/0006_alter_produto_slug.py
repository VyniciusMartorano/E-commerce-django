# Generated by Django 4.0.1 on 2022-01-21 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_rename_variavel_variacao_alter_produto_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]