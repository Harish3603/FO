# Generated by Django 5.0.1 on 2024-03-06 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FO_APP', '0003_dish_restaurant_delete_app_delete_app2'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
