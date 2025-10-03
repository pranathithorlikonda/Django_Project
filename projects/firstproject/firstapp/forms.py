from django import forms
from .models import student,staff,data

class StudentForm(forms.ModelForm):


    class Meta:
        model =student
        fields = '__all__'
        labels = {
            'fullname' : 'Full Name',
            'contactno' : 'Contact No',
            'course' : 'Course',
            'fees' : 'Fee',
            'joinenddate' : 'Course Duration'
        }

    def __init__(self,*args,**kwargs):
        super(StudentForm,self).__init__(*args,**kwargs)
        self.fields['course'].empty_label = "Select"

class staffForm(forms.ModelForm):


    class Meta:
        model = staff
        fields = '__all__'
        labels = {
           'FullName' : 'Full Name',
           'salarypermonth' : 'Salary_per_Month',
            'teachingcourse' : 'Teaching Course'
        }

    def __init__(self,*args,**kwargs):
        super(staffForm,self).__init__(*args,**kwargs)
        self.fields['teachingcourse'].empty_label = "Select"

class course_data(forms.ModelForm):

    class meta:
        model = data
        fields = '__all__'