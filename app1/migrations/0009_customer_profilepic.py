# Generated by Django 4.2.2 on 2023-07-01 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_customer_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
