# Generated by Django 4.2.5 on 2023-09-23 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('file', '0006_rename_file_user_permission_fileuserpermission'),
    ]

    operations = [
        migrations.AddField(
            model_name='fileuserpermission',
            name='comment_permission',
            field=models.BooleanField(default=False),
        ),
    ]
