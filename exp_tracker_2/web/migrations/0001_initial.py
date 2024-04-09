# Generated by Django 3.2.25 on 2024-04-09 19:03

import django.core.validators
from django.db import migrations, models
import exp_tracker_2.web.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exp_tracker_2.web.validators.validate_only_letters])),
                ('last_name', models.CharField(max_length=15, validators=[django.core.validators.MinLengthValidator(2), exp_tracker_2.web.validators.validate_only_letters])),
                ('budget', models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('profile_image', models.ImageField(blank=True, null=True, upload_to='profiles/', validators=[exp_tracker_2.web.validators.MaxFileSizeInMBValidator(5)])),
            ],
        ),
    ]
