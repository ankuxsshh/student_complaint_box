# Generated by Django 4.2.6 on 2023-11-21 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('complaint_box', '0010_alter_complaint_box_register_userimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complaint_box_register',
            name='userimage',
            field=models.ImageField(default='True', max_length=200, upload_to='student_complaint_box/static/user_profiles'),
        ),
    ]
