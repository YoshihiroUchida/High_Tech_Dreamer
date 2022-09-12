# Generated by Django 4.1.1 on 2022-09-12 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subjects', '0004_alter_subject_color'),
        ('users', '0012_alter_customuser_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='subjects',
            field=models.ManyToManyField(null=True, to='subjects.subject'),
        ),
    ]