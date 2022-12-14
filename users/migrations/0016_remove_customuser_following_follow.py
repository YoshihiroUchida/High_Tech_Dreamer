# Generated by Django 4.1.1 on 2022-09-13 05:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_customuser_following'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='following',
        ),
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follow_target', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accept_follow_user', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='do_follow_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
