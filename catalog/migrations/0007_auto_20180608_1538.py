# Generated by Django 2.0.2 on 2018-06-08 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('can_mark_returned', 'Set book as returned'),)},
        ),
    ]
