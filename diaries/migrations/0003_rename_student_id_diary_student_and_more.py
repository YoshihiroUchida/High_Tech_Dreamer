# Generated by Django 4.1 on 2022-09-13 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_diary_subject_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='diary',
            old_name='student_id',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='subject_id',
            new_name='subject',
        ),
        migrations.RenameField(
            model_name='diary',
            old_name='teacher_id',
            new_name='teacher',
        ),
    ]