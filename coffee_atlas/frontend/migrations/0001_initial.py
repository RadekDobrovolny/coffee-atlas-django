# Generated by Django 4.0.6 on 2022-07-12 20:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Processing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Roastery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.country')),
            ],
        ),
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Unknown', max_length=100)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.country')),
            ],
        ),
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('elevation', models.CharField(max_length=100)),
                ('roast_date', models.DateTimeField(verbose_name='Date roasted')),
                ('on_the_shelf', models.BooleanField(default=True)),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.country')),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.farmer')),
                ('processing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.processing')),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.region')),
                ('roastery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.roastery')),
                ('variety', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='frontend.variety')),
            ],
        ),
    ]
