# Generated by Django 4.0.6 on 2022-07-22 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='like_count',
            field=models.IntegerField(default=0, verbose_name='좋아요수'),
        ),
        migrations.AlterField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0, verbose_name='조회수'),
        ),
    ]