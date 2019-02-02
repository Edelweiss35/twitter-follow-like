# Generated by Django 2.1.1 on 2018-09-24 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0007_auto_20180924_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='paypal_email',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Paypal Email'),
        ),
        migrations.AddField(
            model_name='order',
            name='paypal_name',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Paypal Full Name'),
        ),
        migrations.AddField(
            model_name='order',
            name='twitter_email',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Twitter Email'),
        ),
        migrations.AddField(
            model_name='order',
            name='twitter_phone',
            field=models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='Twitter Phone Number'),
        ),
    ]