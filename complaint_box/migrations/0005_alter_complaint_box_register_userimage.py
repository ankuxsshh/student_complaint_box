# Generated by Django 4.2.6 on 2023-10-26 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_box', '0004_alter_complaint_box_register_userphone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_box_register',
            name='userimage',
            field=models.ImageField(default='True', max_length=200, upload_to='student_complaint_box/static/user_profiles'),
        ),
    ]
