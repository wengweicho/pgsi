# Generated by Django 3.1.4 on 2021-01-13 03:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pgworker', '0002_uploadpdf'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_files', models.FileField(blank=True, null=True, upload_to='upload_files/')),
            ],
        ),
        migrations.DeleteModel(
            name='UploadPdf',
        ),
    ]
