# Generated by Django 4.1.1 on 2022-09-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdID', models.IntegerField()),
                ('stdName', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Class',
        ),
    ]
