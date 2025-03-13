# Generated by Django 5.1.2 on 2025-03-10 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('borrowed_by', models.CharField(blank=True, max_length=100, null=True)),
                ('borrow_date', models.DateTimeField(blank=True, null=True)),
                ('genres', models.ManyToManyField(to='library.genre')),
            ],
        ),
    ]
