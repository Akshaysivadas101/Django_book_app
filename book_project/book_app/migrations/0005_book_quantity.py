# Generated by Django 5.0.3 on 2024-05-23 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_app', '0004_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=1234),
            preserve_default=False,
        ),
    ]