from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student/', views.newStudent, name='student'),
    path('teacher/', views.newTeacher, name='teacher'),
    path('course/', views.newCourse, name='course'),
    path('assign-teacher/', views.assignateTeacher, name='assign-teacher'),
    path('exam/', views.newExam, name='exam'),
    path('student-list/', views.studentList, name='student-list'),
    path('course-list', views.courseList, name='course-list'),
    path('update-student/<str:pk>/', views.updateStudent, name='update-student'),
    path('delete-student/<str:pk>/', views.deleteStudent, name='delete-student'),
    path('update-course/<str:pk>/', views.updateCourse, name='update-course'),
    path('delete-course/<str:pk>/', views.deleteCourse, name='delete-course'),
    path('update-exam/<str:pk>/', views.updateExam, name='update-exam'),
    path('delete-exam/<str:pk>/', views.deleteExam, name='delete-exam'),
    path('student-info/<str:pk>/', views.studentInfo, name='student-info'),
]