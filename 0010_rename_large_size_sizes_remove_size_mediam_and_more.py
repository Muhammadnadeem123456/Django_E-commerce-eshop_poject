# Generated by Django 4.2.1 on 2024-02-27 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_size_alter_product_category_alter_signup_last_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='size',
            old_name='large',
            new_name='sizes',
        ),
        migrations.RemoveField(
            model_name='size',
            name='mediam',
        ),
        migrations.RemoveField(
            model_name='size',
            name='small',
        ),
    ]
