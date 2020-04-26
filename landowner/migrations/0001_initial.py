# Generated by Django 3.0.5 on 2020-04-26 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.IntegerField()),
                ('address', models.TextField()),
            ],
        ),
    ]