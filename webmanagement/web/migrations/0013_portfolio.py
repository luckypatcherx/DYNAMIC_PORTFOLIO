# Generated by Django 2.2 on 2023-05-04 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_auto_20230504_2310'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_title', models.CharField(max_length=255)),
                ('portfolio_description', models.TextField()),
                ('portfolio_img', models.ImageField(upload_to='static/portfolio_images/')),
            ],
            options={
                'db_table': 'portfolio',
            },
        ),
    ]