# Generated by Django 4.1.5 on 2023-01-31 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_alter_sizedb_size_num'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact_us_db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(blank=True, max_length=100, null=True)),
                ('contact_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('contact_message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
