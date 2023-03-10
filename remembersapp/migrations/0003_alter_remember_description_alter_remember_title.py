# Generated by Django 4.1.4 on 2022-12-29 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remembersapp', '0002_alter_remember_title_alter_remember_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remember',
            name='description',
            field=models.CharField(blank=True, max_length=512),
        ),
        migrations.AlterField(
            model_name='remember',
            name='title',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
