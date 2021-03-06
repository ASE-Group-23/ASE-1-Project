# Generated by Django 3.0.7 on 2020-07-18 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drive_data', '0002_auto_20200609_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='temp_file_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='file',
            name='file',
            field=models.FileField(default=None, null=True, upload_to='uploads/'),
        ),
    ]
