# Generated by Django 4.2.6 on 2023-10-20 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='')),
                ('description', models.TextField(verbose_name='')),
                ('type_mobil', models.CharField(choices=[('Красный', 'Красный'), ('Белый', 'Белый'), ('Синий', 'Синий'), ('Черный', 'Черный')], max_length=100)),
                ('cost', models.PositiveIntegerField()),
                ('director', models.CharField(max_length=100)),
            ],
        ),
    ]