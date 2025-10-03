from django.urls import path
from firstapp import views

urlpatterns = [
    path('', views.base, name="base_file"),
    path('student/insert/', views.student_form, name="student_insert"),
    path('staff/insert/', views.staff_form, name="staff_insert"),
    path('student/<int:id>', views.student_form, name="student_update"),
    path('staff/<int:id>', views.staff_form, name="staff_update"),
    path('list/', views.student_list, name="student_list"),
    path('list_a/', views.staff_list, name="staff_list"),
    path('students/<int:id>', views.student_delete, name="student_delete"),
    path('staffs/<int:id>', views.staff_delete, name="staff_delete"),

]