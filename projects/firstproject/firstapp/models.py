from django.db import models

# Create your models here.

class Course(models.Model):
    Course = models.CharField(max_length=400)

    def __str__(self):
        return self.Course


class student(models.Model):
    fullname = models.CharField(max_length=150)
    contactno = models.CharField(max_length=50)
    course = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)
    fees = models.CharField(max_length=50)


class staff(models.Model):
    FullName = models.CharField(max_length=200)
    salarypermonth = models.CharField(max_length=100)
    teachingcourse = models.ForeignKey(Course,on_delete=models.CASCADE,null=True)

class data(models.Model):
    course_name = models.CharField(max_length=400)
    technologies = models.CharField()
    time = models.CharField(max_length=300)
    fee = models.CharField(max_length=100)

