# Generated by Django 4.0.6 on 2022-08-01 10:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0002_books_borrowed'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='borrow_book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed', models.BooleanField(default=False)),
                ('borrowed_on', models.DateField(auto_now_add=True)),
                ('retrieve_on', models.DateField()),
                ('fine', models.BooleanField(default=False)),
                ('book', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='books.books')),
                ('borrower', models.ForeignKey(max_length=100, on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
        ),
    ]
