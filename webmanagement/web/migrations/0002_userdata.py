# Generated by Django 4.1.8 on 2023-04-09 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Name', models.CharField(max_length=45)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'userdata',
            },
        ),
    ]
