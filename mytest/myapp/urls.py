from django.urls import path

from .views import *

app_name = 'myapp'

urlpatterns = [
    path('professors/', professor_list, name='professor_list'),
    path('professors/create/', create_professor, name='create_professor'),
    path('professors/update/<int:pk>/', update_professor, name='update_professor'),
    path('professors/delete/<int:pk>/', delete_professor, name='delete_professor'),

    path('students/', student_list, name='student_list'),
    path('students/create/', create_student, name='create_student'),
    path('students/update/<int:pk>/', update_student, name='update_student'),
    path('students/delete/<int:pk>/', delete_student, name='delete_student'),
    path('students/status/<int:student_id>/', student_status_view, name='student_status'),

    path('supervisors/', supervisor_list, name='supervisor_list'),
    path('supervisors/create/', create_supervisor, name='create_supervisor'),
    path('supervisors/update/<int:pk>/', update_supervisor, name='update_supervisor'),
    path('supervisors/delete/<int:pk>/', delete_supervisor, name='delete_supervisor'),

    path('courses/', course_list, name='course_list'),
    path('courses/create/', create_course, name='create_course'),
    path('courses/update/<int:pk>/', update_course, name='update_course'),
    path('courses/delete/<int:pk>/', delete_course, name='delete_course'),

    path('learningprograms/', learningprogram_list, name='learningprogram_list'),
    path('learningprograms/create/', create_learningprogram, name='create_learningprogram'),
    path('learningprograms/update/<int:pk>/', update_learningprogram, name='update_learningprogram'),
    path('learningprograms/delete/<int:pk>/', delete_learningprogram, name='delete_learningprogram'),

    path('student-status/<int:student_id>/', student_status_view, name='student-status'),
]
