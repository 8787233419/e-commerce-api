# Generated by Django 5.1.4 on 2025-01-24 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_product_product_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pwdhistory',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userlogin',
            name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='id',
        ),
        migrations.RemoveField(
            model_name='product',
            name='id',
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='category',
            name='cat_name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='order',
        ),
        migrations.DeleteModel(
            name='PwdHistory',
        ),
        migrations.DeleteModel(
            name='userlogin',
        ),
    ]
