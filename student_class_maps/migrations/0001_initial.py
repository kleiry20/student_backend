# Generated by Django 4.1.1 on 2022-09-18 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('students', '0001_initial'),
        ('classes', '0003_alter_standard_stdid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student_Class_Map',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stdID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.standard')),
                ('studID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.student')),
            ],
        ),
    ]
