# Generated by Django 4.2.13 on 2024-07-17 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ideas", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="idea",
            name="devtool",
        ),
        migrations.AlterField(
            model_name="idea",
            name="interest",
            field=models.IntegerField(default=0, verbose_name="아이디어 관심도"),
        ),
    ]
