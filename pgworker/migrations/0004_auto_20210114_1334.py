# Generated by Django 3.1.5 on 2021-01-14 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgworker', '0003_auto_20210113_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='upload_files',
            field=models.FileField(blank=True, null=True, upload_to='mysite/'),
        ),
    ]
