from django.db import models
# Create your models here.

class complaint_box_register(models.Model):
    id = models.AutoField(primary_key=True)
    userimage = models.ImageField(upload_to='student_complaint_box/static/user_profiles', max_length=200, default="True")
    useremail = models.CharField(max_length=200, default=True)
    username = models.CharField(max_length=200)
    userphone = models.CharField(max_length=10,default="True")
    password = models.CharField(max_length=200)

class complaint_box_complaint(models.Model):
    id = models.AutoField(primary_key=True)
    userid = models.CharField(max_length=200)
    complaintto = models.CharField(max_length=200)
    date = models.DateField() 
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200) 
    complaintmessage = models.CharField(max_length=200)
    status = models.CharField(max_length=200)

class complaint_box_faculty(models.Model):
     id = models.AutoField(primary_key=True)
     designation =models.CharField(max_length=200)
     name = models.CharField(max_length=200)
     email = models.CharField(max_length=200,unique=True)
     password = models.CharField(max_length=200)
    
class complaint_box_acknowledgement(models.Model):
     id = models.AutoField(primary_key=True)
     date = models.CharField(max_length=200)
     name = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     acknowledgement_message = models.CharField(max_length=200)

class complaint_box_faculty_acknowledgement(models.Model):
     id = models.AutoField(primary_key=True)
     date = models.CharField(max_length=200)
     designation =models.CharField(max_length=200)
     name = models.CharField(max_length=200)
     email = models.CharField(max_length=200)
     acknowledgement_message = models.CharField(max_length=200)


   