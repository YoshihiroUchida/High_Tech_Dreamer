# Generated by Django 4.1 on 2022-09-10 10:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_customuser_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='juku',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.juku'),
            preserve_default=False,
        ),
    ]
