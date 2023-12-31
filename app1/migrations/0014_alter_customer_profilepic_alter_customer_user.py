# Generated by Django 4.2.2 on 2023-07-01 12:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app1', '0013_customer_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(blank=True, default='www.png', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
