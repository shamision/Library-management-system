# Generated by Django 4.0.6 on 2022-08-08 09:59

import BorrowBooks.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BorrowBooks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow_book',
            name='retrieve_on',
            field=models.DateField(default=BorrowBooks.models.expiring_date),
        ),
    ]