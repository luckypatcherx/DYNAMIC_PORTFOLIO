# Generated by Django 4.1.8 on 2023-04-09 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_userdata_phno'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdata',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
