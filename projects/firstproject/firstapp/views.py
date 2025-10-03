from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import StudentForm,staffForm
from .models import staff,student,data

# Create your views here.
def base(request):
    information = {'courses':data.objects.all()}
    return render(request,'html_files/base.html',information)

def student_list(request):
    context = {'student_list':student.objects.all()}
    return render(request,'html_files/student_list.html',context)

def student_form(request,id = 0):
    if request.method == "GET":
        if id == 0:
            form = StudentForm()
        else:
            students = student.objects.get(pk=id)
            form = StudentForm(instance=students)  
        return render(request,"html_files/student_form.html",{'form':form})
    else:
        if id ==0:
            form = StudentForm(request.POST)
        else:
            students = student.objects.get(pk=id)
            form = StudentForm(request.POST,instance=students)
        if form.is_valid():
            form.save()
        return redirect('/list')

def student_delete(request,id):
    delete_student = student.objects.get(pk=id)
    delete_student.delete()
    return redirect('/list')

def staff_list(request):
    context = {'staff_list':staff.objects.all()}
    return render(request,'html_files/staff_list.html',context)

def staff_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = staffForm()
        else:
            staffs = staff.objects.get(pk=id)
            form = staffForm(instance=staffs)
        return render(request, "html_files/staff_form.html", {'form': form})
    else:
        if id == 0:
            form = staffForm(request.POST)
        else:
            staffs = staff.objects.get(pk=id)
            form = staffForm(request.POST, instance=staffs)

        if form.is_valid():
            form.save()
        return redirect('/list_a')

def staff_delete(request,id):
    delete_staff = staff.objects.get(pk=id)
    delete_staff.delete()
    return redirect('/list_a')
