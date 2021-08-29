# Generated by Django 3.2.3 on 2021-08-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_order_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('information', models.TextField(max_length=10000)),
                ('image', models.ImageField(default='', upload_to='uploads/products/')),
            ],
        ),
    ]