# Generated by Django 3.2.23 on 2023-11-30 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artists',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(blank=True, max_length=254, null=True)),
                ('profile_info', models.TextField()),
            ],
        ),
    ]
