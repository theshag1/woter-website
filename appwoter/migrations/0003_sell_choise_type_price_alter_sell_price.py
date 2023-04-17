# Generated by Django 4.2 on 2023-04-12 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appwoter', '0002_alter_sell_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='sell',
            name='choise_type_price',
            field=models.FloatField(choices=[('cash', 'Cash'), ('free', 'Free'), ('exchange', 'Exchange')], default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='sell',
            name='price',
            field=models.FloatField(),
        ),
    ]
