# Generated by Django 3.2.9 on 2021-11-07 11:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0007_alter_checkout_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='product', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='status',
            field=models.CharField(choices=[('In stock', 'В наличии'), ('Out of stock', 'Нет в наличии'), ('Awaiting', 'Ожидается')], max_length=30),
        ),
    ]