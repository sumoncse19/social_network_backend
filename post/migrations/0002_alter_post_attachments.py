# Generated by Django 4.2.5 on 2023-09-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='attachments',
            field=models.ManyToManyField(blank=True, to='post.postattachment'),
        ),
    ]