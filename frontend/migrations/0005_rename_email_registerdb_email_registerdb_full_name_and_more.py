# Generated by Django 4.1.5 on 2023-01-30 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0004_delete_cartdb'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerdb',
            old_name='email',
            new_name='Email',
        ),
        migrations.AddField(
            model_name='registerdb',
            name='full_name',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='registerdb',
            name='mobile_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
