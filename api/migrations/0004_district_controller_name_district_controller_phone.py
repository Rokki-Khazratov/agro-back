# Generated by Django 5.0.2 on 2024-10-26 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_district_region_delete_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='controller_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='controller_phone',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]