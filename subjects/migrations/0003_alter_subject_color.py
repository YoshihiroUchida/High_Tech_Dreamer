# Generated by Django 4.1 on 2022-09-11 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0002_subject_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='color',
            field=models.CharField(choices=[('red', 'danger'), ('blue', 'blue'), ('yellow', 'yellow'), ('green', 'green'), ('green', 'green'), ('gray', 'gray'), ('black', 'black'), ('white', 'white')], max_length=20, verbose_name='色'),
        ),
    ]
