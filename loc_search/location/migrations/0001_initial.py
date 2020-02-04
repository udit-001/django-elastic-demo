# Generated by Django 2.2 on 2020-01-15 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(blank=True, max_length=255, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=255, null=True)),
                ('place_name', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_name1', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_code1', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_name2', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_code2', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_name3', models.CharField(blank=True, max_length=255, null=True)),
                ('admin_code3', models.CharField(blank=True, max_length=255, null=True)),
                ('latitude', models.CharField(blank=True, max_length=255, null=True)),
                ('longitude', models.CharField(blank=True, max_length=255, null=True)),
                ('accuracy', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
