# Generated by Django 4.2.16 on 2024-11-10 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_name', models.CharField(max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('quantity', models.IntegerField(default=0)),
                ('order_date', models.DateField()),
            ],
        ),
    ]
