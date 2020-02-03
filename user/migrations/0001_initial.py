# Generated by Django 2.2.2 on 2020-01-22 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('post_title', models.CharField(max_length=50)),
                ('post_content', models.TextField(default='tutorial content')),
                ('date_published', models.DateField(blank=True, null=True)),
                ('user_profile_link', models.DateField(blank=True, null=True)),
            ],
        ),
    ]