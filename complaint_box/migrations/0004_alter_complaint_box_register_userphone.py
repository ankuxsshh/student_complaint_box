# Generated by Django 4.2.6 on 2023-10-25 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_box', '0003_complaint_box_acknowledgement_complaint_box_faculty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_box_register',
            name='userphone',
            field=models.CharField(default='True', max_length=10),
        ),
    ]
