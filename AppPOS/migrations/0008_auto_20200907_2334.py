# Generated by Django 3.1.1 on 2020-09-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppPOS', '0007_auto_20200907_0052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
