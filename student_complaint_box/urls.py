"""
URL configuration for student_complaint_box project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from complaint_box import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="index"),
    path('student_index_page/',views.student_index_page,name="student_index_page"),
    path('student_index_page/student_login_page/',views.student_login_page,name="student_login_page"),
    path('student_index_page/student_login_page/student_register_page/',views.student_register_page,name="student_register_page"),
    path('register_user/',views.register_user,name="register_user"),

#STUDENT_PORTAL :
    path('student_login_page/', views.student_login_page, name="student_login_page"),
    path('authenticate_user/',views.authenticate_user,name="authenticate_user"),
    path('student_home_page/',views.student_home_page,name="student_home_page"),
    path('student_home_page/student_complaint_page/',views.student_complaint_page,name="student_complaint_page"),
    path('register_complaint/',views.register_complaint,name="register_complaint"),
    path('student_complaint_page/',views.student_complaint_page,name="student_complaint_page"),
    path('student_home_page/student_acknowledgement_page/', views.student_acknowledgement_page, name="student_acknowledgement_page"),
    path('student_home_page/student_profile_page/', views.student_profile_page, name="student_profile_page"),
    path('update_user/', views.update_user, name='update_user'),
    path('student_home_page/student_updateprofile_page/', views.student_updateprofile_page, name="student_updateprofile_page"),
    path('student_home_page/student_logout_page/', views.student_logout_page, name="student_logout_page"),

#ADMIN_PORTAL : 
    path('admin_index_page/',views.admin_index_page, name="admin_index_page"),
    path('admin_index_page/admin_login_page/', views.admin_login_page, name="admin_login_page"),
    path('authenticate_user/', views.authenticate_user, name="authenticate_user"),
    path('admin_home_page/', views.admin_home_page, name="admin_home_page"),
    path('admin_home_page/admin_viewstudent_page', views.admin_viewstudent_page, name="admin_viewstudent_page"),
    path('admin_home_page/admin_viewstudent_page/delete_student/<int:student_id>/', views.delete_student, name="delete_student"),
    path('admin_home_page/admin_addfaculty_page', views.admin_addfaculty_page, name="admin_addfaculty_page"),
    path('add_faculty/', views.add_faculty, name="add_faculty"),
    path('admin_addfaculty_page', views.admin_addfaculty_page, name="admin_addfaculty_page"),
    path('admin_home_page/admin_viewfaculty_page', views.admin_viewfaculty_page, name="admin_viewfaculty_page"),
    path('admin_home_page/admin_acknowledgement_page/', views.admin_acknowledgement_page, name="admin_acknowledgement_page"),
    path('save_acknowledgement/', views.save_acknowledgement, name="save_acknowledgement"),
    path('admin_acknowledgement_page/', views.admin_acknowledgement_page, name="admin_acknowledgement_page"),
    path('admin_home_page/admin_viewprofile_page/', views.admin_viewprofile_page, name="admin_viewprofile_page"),
    path('admin_home_page/admin_logout_page', views.admin_logout_page, name="admin_logout_page"),    

#FACULTY_PORTAL :
    path('faculty_index_page/', views.faculty_index_page, name="faculty_index_page"),
    path('faculty_index_page/faculty_login_page/', views.faculty_login_page,name="faculty_login_page"),
    path('authenticate_user/', views.authenticate_user, name="authenticate_user"),
    path('faculty_home_page/', views.faculty_home_page, name="faculty_home_page"),
    path('faculty_home_page/faculty_viewcomplaint_page/', views.faculty_viewcomplaint_page, name="faculty_viewcomplaint_page"),
    path('faculty_home_page/faculty_acknowledgement_page/', views.faculty_acknowledgement_page, name="faculty_acknowledgement_page"),
    path('send_acknowledgement/', views.send_acknowledgement, name="send_acknowledgement"),
    path('faculty_acknowledgement_page/', views.faculty_acknowledgement_page, name="faculty_acknowledgement_page"),
    path('faculty_home_page/faculty_adminacknowledgement_page/', views.faculty_adminacknowledgement_page, name="faculty_adminacknowledgement_page"),
    path('faculty_home_page/faculty_viewprofile_page/', views.faculty_viewprofile_page, name="faculty_viewprofile_page"),
    path('faculty_home_page/faculty_logout_page/', views.faculty_logout_page, name="faculty_logout_page"),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
