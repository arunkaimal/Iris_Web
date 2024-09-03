# Generated by Django 5.0.6 on 2024-07-03 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('irisapp', '0002_lifestyle_wedding_products_sports'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lifestyle_wedding',
            name='life_wed_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='products',
            name='product_image',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='sports',
            name='sport_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
