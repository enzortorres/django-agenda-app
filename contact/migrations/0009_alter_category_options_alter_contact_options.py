# Generated by Django 5.2 on 2025-04-21 20:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0008_alter_category_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'Contact', 'verbose_name_plural': 'Contacts'},
        ),
    ]
