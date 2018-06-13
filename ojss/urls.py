"""ojss URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from ojss_app import views
from  django.contrib.auth.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.UserController.login, name='index'),
    path("search", views.UserController.show_home_page, name='search'),
    path("job_details/<int:job_id>",views.ApplicationController.job_details, name="job_details"),
    path("apply/<int:job_id>", views.ApplicationController.apply, name='apply'),
    path("see_applications", views.ApplicationController.my_applications, name="my_applications"),
    path("seeker_register",views.UserController.seekerRegister, name='seeker_register'),
    path("recruiter_register", views.UserController.recruiterRegister, name='recruiter_register'),
    path("^search?", views.SearchController.search_for_jobs, name="search_list"),
    path("seekerprofile",views.UserController.seekerProfile, name= 'seeker_profile'),
    path("recruiterprofile",views.UserController.recruiterProfile, name='recruiter_profile'),
    path("skills",views.UserController.add_skills, name='skills'),
    path("add_jobs", views.JobController.add_job, name='add_job'),
    path("manage_jobs", views.JobController.manage_jobs, name='manage_jobs'),
    path('job_edit/<int:job_id>', views.JobController.edit_job, name='job_edit'),
    path('applications/<int:application_id>',views.JobController.applications, name='applications'),
    path('applicant_details/<int:job_id>/<int:seeker_profile_id>',
         views.JobController.applicant_details, name='applicant_details'),
    path('accept_applicant/<int:application_id>',views.JobController.accept_applicant, name='accept_applicant'),
    path('reject_applicant/<int:application_id>',views.JobController.reject_applicant, name='reject_applicant'),
    path('logout', views.UserController.logout_user, name='logout'),
    path('ajax/load_subcategory',views.AjaxRequestController.subcategory, name='subcategory'),
    path('interview_call/<int:application_id>', views.JobController.interview_call, name='send_interview_call'),
    path('ajax/load_category', views.AjaxRequestController.category, name='category')
]
