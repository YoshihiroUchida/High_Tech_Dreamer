# Generated by Django 4.1.1 on 2022-09-12 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_customuser_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='birth',
            field=models.DateField(null=True, verbose_name='生年月日'),
        ),
    ]
