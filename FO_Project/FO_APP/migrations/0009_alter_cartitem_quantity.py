# Generated by Django 5.0.1 on 2024-03-11 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FO_APP', '0008_remove_cartitem_user_alter_cartitem_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]