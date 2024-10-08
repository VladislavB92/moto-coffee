# Generated by Django 5.1.1 on 2024-09-16 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('brand', models.CharField(max_length=50)),
                ('roast_level', models.IntegerField(default=0)),
                ('acidity', models.IntegerField(default=0)),
                ('country_of_origin', models.CharField(max_length=50)),
            ],
        ),
    ]
