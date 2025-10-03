from django.contrib import admin
from .models import Course,student,staff,data

# Register your models here.

admin.site.register(Course)
admin.site.register(student)
admin.site.register(staff)
admin.site.register(data)
