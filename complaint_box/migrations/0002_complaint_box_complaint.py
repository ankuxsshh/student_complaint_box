# Generated by Django 4.2.6 on 2023-10-24 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_box', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='complaint_box_complaint',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('userid', models.CharField(max_length=200)),
                ('complaintto', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('complaintmessage', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
