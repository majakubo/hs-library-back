# Generated by Django 2.0 on 2017-12-09 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='tags',
            field=models.ManyToManyField(default=None, to='books.Tag'),
        ),
    ]