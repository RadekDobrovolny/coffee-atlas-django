# Generated by Django 4.0.6 on 2022-07-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0002_alter_country_options_alter_roastery_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coffee',
            name='coffee_image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='images/'),
        ),
    ]
