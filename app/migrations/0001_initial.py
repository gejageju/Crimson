# Generated by Django 4.0.1 on 2023-01-01 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('amount', models.IntegerField()),
                ('date', models.DateField(auto_now_add=True, verbose_name='Conversation Date')),
                ('time', models.TimeField(auto_now_add=True, verbose_name='Conversation Time')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('price', models.IntegerField(default=0)),
                ('url', models.CharField(max_length=255)),
                ('claimed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Rewards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coins', models.IntegerField()),
            ],
        ),
    ]
