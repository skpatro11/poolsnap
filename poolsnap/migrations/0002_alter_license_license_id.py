# Generated by Django 3.2.8 on 2021-10-13 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poolsnap', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='license',
            name='license_id',
            field=models.CharField(blank=True, editable=False, max_length=12),
        ),
    ]