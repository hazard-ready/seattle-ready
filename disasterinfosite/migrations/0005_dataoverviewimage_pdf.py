# Generated by Django 4.0.8 on 2023-03-03 21:26

import disasterinfosite.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0004_dataoverviewimage_link_text_ar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='dataoverviewimage',
            name='pdf',
            field=models.FileField(null=True, storage=disasterinfosite.models.OverwriteStorage(), upload_to='data'),
        ),
    ]
