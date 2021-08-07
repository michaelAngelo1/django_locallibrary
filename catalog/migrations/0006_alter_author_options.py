# Generated by Django 3.2.4 on 2021-08-06 05:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_author_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name'], 'permissions': (('can_view_author_list', 'View author list'), ('can_view_author_update', 'View author update'))},
        ),
    ]