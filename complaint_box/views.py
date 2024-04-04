from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse
from . import models
from django.core.files.storage import FileSystemStorage
import os
from django.contrib.auth import authenticate, login
from datetime import datetime

# Create your views here.

#STUDENT PORTAL:

def index(request):
    return render(request,'index.html', {})

def student_index_page(request):
     return render(request, 'student/student_index.html', {})

def student_login_page(request):
     return render(request, 'student/student_login.html', {})

def student_register_page(request):
     return render(request, 'student/student_register.html', {})
 
def register_user(request):
    username = request.POST.get("name")
    useremail = request.POST.get("email")
    userphone = request.POST.get("phone")
    password = request.POST.get("password")
    userimage = request.FILES["image"]
    if userimage:
        path = os.path.join(os.getcwd(), "student_complaint_box/static/user_profiles", useremail.split("@")[0])
        os.makedirs(path)
        image_file = FileSystemStorage(path)
        image_file.save(userimage.name, userimage)
        cbr_obj = models.complaint_box_register(
            userimage=userimage,
            useremail=useremail,
            username=username,
            userphone=userphone,  
            password=password
        )
        cbr_obj.save()
        return HttpResponse('<script>alert("User Registered Successfully");window.location.href="/student_login_page/";</script>', content_type='text/html')
    else:
        return HttpResponse('<script>alert("Invalid Registration");window.location.href="/student_register_page/";</script>', content_type='text/html')

def authenticate_user(request):
    email = request.POST.get("email")
    password = request.POST.get("password")
    
    # Check if the login is for a student
    cbr_obj = models.complaint_box_register.objects.filter(useremail=email, password=password).first()
    if cbr_obj:
        request.session["id"] = cbr_obj.id
        request.session["email"] = cbr_obj.useremail
        return HttpResponse('<script>alert("Welcome ' + cbr_obj.username + '");window.location.href = "/student_home_page/";</script>',content_type='text/html')
   
    # Check if the login is for an admin
    elif email == 'admin@gmail.com' and password == 'admin':
        request.session['logindetails'] = email
        request.session['admin'] = 'admin'
        return HttpResponse('<script>alert("Welcome ' + "admin" + '");window.location.href = "/admin_home_page/";</script>',content_type='text/html')
    
    # Check if the login is for a faculty member
    else:
        cbz_obj = models.complaint_box_faculty.objects.filter(email=email, password=password).first()
        if cbz_obj:
            request.session["id"] = cbz_obj.id
            request.session["email"] = cbz_obj.email
            return HttpResponse('<script>alert("Welcome ' + cbz_obj.name + '");window.location.href = "/faculty_home_page/";</script>', content_type='text/html')
    return HttpResponse('<script>alert("Invalid user or password");window.location.href = "";</script>', content_type='text/html')
    
def student_home_page(request):
    return render(request, 'student/student_home.html', {})

def student_complaint_page(request):
     return render(request, 'student/complaint.html', {})


def register_complaint(request):
    if request.method == 'POST':
        userid = request.POST.get("userid")
        complaintto = request.POST.get("complaintto")
        date = request.POST.get("date")
        name = request.POST.get("name")
        email = request.POST.get("email")
        complaintmessage = request.POST.get("complaintmessage")
        status = request.POST.get("status")

        complaint = models.complaint_box_complaint(
            userid=userid,
            complaintto=complaintto,
            date=date,
            name=name,
            email=email,
            complaintmessage=complaintmessage,
            status=status,
        )
        complaint.save()
        return HttpResponse('<script>alert("Complaint Registered");window.location.href = "/student_home_page/student_complaint_page/";</script>', content_type='text/html')
    else:
        faculty_members = models.complaint_box_faculty.objects.all()
        context = {
            'faculty_members': faculty_members,
        }
        return render(request, 'complaint.html', context)


def student_acknowledgement_page(request):
    acknowledgements = models.complaint_box_acknowledgement.objects.all()
    context = {
        'acknowledgements': acknowledgements
    }
    return render(request, 'student/acknowledgement.html', context)

def student_profile_page(request):
    cbr_obj = models.complaint_box_register.objects.filter(id=request.session["id"]).first()
    useremail = cbr_obj.useremail
    username = cbr_obj.username
    userphone = cbr_obj.userphone
    password = cbr_obj.password
    userimage = cbr_obj.userimage 
    return render(request, 'student/student_viewprofile.html', {
        "username": username,
        "useremail": useremail,
        "userphone": userphone,
        "password": password,
        "userimage": userimage, 
    })

def student_updateprofile_page(request):
    user_id = request.session.get("id")
    if user_id is not None:
        cbr_obj = models.complaint_box_register.objects.get(id=user_id)
        return render(request, 'student/student_updateprofile.html', {
            "cbr_obj": cbr_obj,
        })
    else:
        # Handle the case where user_id is not available in the session
        return HttpResponse("User not found.")
    
    
def update_user(request):
    if request.method == "POST":
        user_id = request.session.get("id")
        if user_id is not None:
            cbr_obj = models.complaint_box_register.objects.get(id=user_id)
            try:
                image = request.FILES["image"]
                if image:
                    path = os.path.join(os.getcwd(), "student_complaint_box/static/user_profiles", cbr_obj.useremail.split("@")[0])
                    os.makedirs(path, exist_ok=True)
                    image_file = FileSystemStorage(path)
                    filename = image_file.save(image.name, image)
                    cbr_obj.userimage = os.path.join(path, filename)
            except:
                pass
            name = request.POST.get("name")
            email = request.POST.get("email")
            phone = request.POST.get("phone")
            password = request.POST.get("password")

            if email:
                cbr_obj.useremail = email
            if name:
                cbr_obj.username = name
            if phone:
                cbr_obj.userphone = phone
            if password:
                cbr_obj.password = password

            cbr_obj.save()
            return redirect('student_viewprofile_page')

    return render(request, 'student/student_updateprofile.html')


def delete(request, id):
    member = models.complaint_box_register.objects.get(id=id)
    member.delete()
    return render(request, 'student/student_profile_page.html')

def student_logout_page(request):
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    return render(request, 'index.html')

#ADMIN PORTAL:

def admin_index_page(request):
    return render(request, 'admin/admin_index.html', {})

def admin_login_page(request):
    return render(request, 'admin/admin_login.html',{} )

def admin_home_page(request):
    return render(request, 'admin/admin_home.html', {} )

def admin_viewstudent_page(request):
    complaints = models.complaint_box_complaint.objects.all()
    students = models.complaint_box_register.objects.all()
    context = {
        'complaints': complaints,
        'students': students,
    }
    return render(request, 'admin/admin_viewstudent.html', context)


def delete_student(request, student_id):
    student = models.complaint_box_register.objects.get(id=student_id)
    student.delete()
    return render(request,'admin_viewstudent_page')


def admin_addfaculty_page(request):
     return render(request, 'admin/admin_addfaculty.html', {} )


def add_faculty(request):
    if request.method == 'POST':
        # Get data from the POST request
        designation = request.POST.get("facultyType")  # Use the correct field name
        name = request.POST.get("facultyName")  # Use the correct field name
        email = request.POST.get("facultyEmail")  # Use the correct field name
        password = request.POST.get("facultyPassword")  # Use the correct field name
        faculty_member = models.complaint_box_faculty.objects.create(
            designation=designation,
            name=name,
            email=email,
            password=password
        )
        # Redirect to a success page or provide a success message
        return HttpResponse('<script>alert("Faculty Added Successfully");window.location.href="admin_viewfaculty_page";</script>', content_type='text/html')
    else:
        # If the request method is not POST, render a page where the admin can input faculty details
        return HttpResponse('<script>alert("Faculty not registered");window.location.href="/admin_home_page/admin_addfaculty_page/";</script>', content_type='text/html')

    
def admin_viewfaculty_page(request):
    # Retrieve all faculty members from the database
    faculties = models.complaint_box_faculty.objects.all()
    # Pass the faculties to the template for rendering
    context = {
        'faculties': faculties
    }
    return render(request, 'admin/admin_viewfaculty.html', context)

def admin_acknowledgement_page(request):
    return render(request, 'admin/admin_acknowledgement.html', {})

def save_acknowledgement(request):
    if request.method == 'POST':
        # Assuming 'facultyType' is the faculty type sent from the form
        date = request.POST.get('date')
        designation = request.POST.get('facultyType')  # Using facultyType as designation
        name = request.POST.get('name')
        email = request.POST.get('email')
        acknowledgement_message = request.POST.get('acknowledgement_message')
        acknowledgement = models.complaint_box_faculty_acknowledgement.objects.create(
                date=date,
                designation=designation,
                name=name,
                email=email,
                acknowledgement_message=acknowledgement_message
            )
        acknowledgement.save()
        # Redirect to the admin_acknowledgement_page with a success message
        return HttpResponse('<script>alert("Acknowledgement Sent");window.location.href="/admin_acknowledgement_page";</script>', content_type='text/html')
    
    # If the request method is not POST, render the admin_acknowledgement_page
    return render(request, 'admin/admin_acknowledgement.html')


def admin_viewprofile_page(request):
    return render(request, 'admin/admin_viewprofile.html',{})
    
def admin_logout_page(request):
    # Clear the session by deleting all keys
    session_keys = list(request.session.keys())
    for key in session_keys:
        del request.session[key]
    # Render the 'index.html' template
    return render(request, 'index.html')


#FACULTY PORTAL:

def faculty_index_page(request):
    return render(request,'faculty/faculty_index.html', {})

def faculty_login_page(request):
    return render(request,'faculty/faculty_login.html',{} )

def faculty_home_page(request):
    return render(request, 'faculty/faculty_home.html', {})

def faculty_viewcomplaint_page(request):
    complaints = models.complaint_box_complaint.objects.all()
    students = models.complaint_box_register.objects.all()
    context = {
        'complaints': complaints,
        'students': students,
    }
    return render(request, 'faculty/faculty_viewcomplaint.html', context)

def faculty_acknowledgement_page(request):
    return render(request, 'faculty/faculty_acknowledgement.html', {})

def send_acknowledgement(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        name = request.POST.get('name')
        email = request.POST.get('email')
        acknowledgement_message = request.POST.get('acknowledgement_message')

        acknowledgement = models.complaint_box_acknowledgement(
            date=date,
            name=name,
            email=email,
            acknowledgement_message=acknowledgement_message,
        )
        acknowledgement.save()

        return HttpResponse('<script>alert("Acknowledgement Sent");window.location.href="/faculty_acknowledgement_page";</script>', content_type='text/html')

    return render(request, 'faculty/faculty_acknowledgement.html', {})


def faculty_adminacknowledgement_page(request):
    acknowledgements = models.complaint_box_faculty_acknowledgement.objects.all()
    context = {
        'acknowledgements': acknowledgements,
    }
    return render(request, 'faculty/faculty_adminacknowledgement.html', context)

def faculty_viewprofile_page(request):
    cbz_obj = models.complaint_box_faculty.objects.filter(id = request.session["id"]).first()
    email = cbz_obj.email
    designation= cbz_obj.designation
    name = cbz_obj.name
    password = cbz_obj.password
    return render(request, 'faculty/faculty_viewprofile.html', {"name": name, "designation": designation, "email": email,  "password": password})  

def faculty_logout_page(request):
    return render(request,'faculty/faculty_logout.html', {})


