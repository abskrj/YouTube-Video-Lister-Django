# Generated by Django 3.1.2 on 2020-10-01 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lister', '0004_videodetails_videoid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videodetails',
            name='publishedAt',
            field=models.DateTimeField(),
        ),
    ]
