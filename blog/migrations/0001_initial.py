# Generated by Django 2.2 on 2019-04-29 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('brief', models.TextField()),
                ('content', models.TextField()),
                ('publish_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
