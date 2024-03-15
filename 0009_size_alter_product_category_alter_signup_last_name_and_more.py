# Generated by Django 4.2.1 on 2024-02-27 14:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_rename_frist_name_signup_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('small', models.BooleanField()),
                ('mediam', models.BooleanField()),
                ('large', models.BooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='last_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='product',
            name='available_sizes',
            field=models.ManyToManyField(blank=True, null=True, to='store.size'),
        ),
    ]
