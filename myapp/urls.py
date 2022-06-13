from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.LoginAPI.as_view()),

    # -------------------admin--------------------------------
    path('admin-profile/',views.ProfileViewAPI.as_view()),
    path('hr-view/',views.HrviewAPI.as_view()),
    path('hr-edit/<int:pk>',views.HrEditAPI.as_view()),
    path('hr-delete/<int:pk>',views.HrDeleteAPI.as_view()),
    path('admin-app',views.ApplicationAPI.as_view()),

    # ----------------------hr-----------------------------
    path('register/',views.RegisterAPI.as_view()),
    path('hr-profile/<int:pk>',views.HrProfileAPI.as_view()),
    path('job-post/',views.JobPostAPI.as_view()),
    path('job-view/',views.JobViewAPI.as_view()),
    path('job-edit/<int:pk>',views.JobEditAPI.as_view()),
    path('job-delete/<int:pk>',views.JobDeleteAPI.as_view()),
    path('hr-app/',views.ApplicationHr.as_view()),
    # ----------------------Job-seeker------------------------
    path('apply/',views.ApplyAPI.as_view()),

]