# Generated by Django 2.0.2 on 2018-03-15 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_book_reviews'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='reviews',
        ),
    ]
