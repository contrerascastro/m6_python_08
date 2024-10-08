# Generated by Django 5.0.6 on 2024-07-04 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField()),
                ('image_url', models.URLField()),
                ('shortName', models.SlugField()),
                ('is_private', models.BooleanField()),
            ],
        ),
    ]
