# Generated by Django 4.1.7 on 2023-03-29 05:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_bookinstance_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookinstance',
            options={'ordering': ['due_back'], 'permissions': (('Can mark returned', 'Set book as returned'),)},
        ),
    ]
