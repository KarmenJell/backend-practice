# Generated by Django 5.0.6 on 2024-06-10 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('token_fetcher', '0003_alter_token_symbol'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='symbol',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]