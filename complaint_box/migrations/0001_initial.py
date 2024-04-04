# Generated by Django 4.2.6 on 2023-10-24 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='complaint_box_register',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userimage', models.ImageField(max_length=200, unique=True, upload_to='student_complaint_box/static/user_profiles')),
                ('useremail', models.CharField(max_length=200, unique=True)),
                ('username', models.CharField(max_length=200)),
                ('userphone', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
    ]
