# Generated by Django 3.1.2 on 2022-02-03 15:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('receitas', '0003_receita_publicada'),
    ]

    operations = [
        migrations.AddField(
            model_name='receita',
            name='foto_receita',
            field=models.ImageField(blank=True, upload_to='fotos/%d/%m/%Y'),
        ),
    ]
