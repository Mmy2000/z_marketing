# Generated by Django 4.2.13 on 2024-05-22 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_newslitter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='setting/')),
            ],
        ),
    ]
