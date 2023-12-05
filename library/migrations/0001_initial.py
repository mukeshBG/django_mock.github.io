# Generated by Django 4.2.7 on 2023-12-05 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('genre', models.CharField(default='none', max_length=20)),
                ('isbn', models.IntegerField()),
                ('availability_status', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Patron_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=55)),
                ('contact_info', models.CharField(max_length=200)),
                ('membership_details', models.CharField(default='normal', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Borrowing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowing_date', models.DateTimeField(auto_now_add=True)),
                ('return_date', models.DateTimeField()),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.patron_management')),
                ('title', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book_management')),
            ],
        ),
    ]