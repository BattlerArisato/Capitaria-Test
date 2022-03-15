from django.forms import ModelForm
from .models import Student, Teacher, Course, Exam, TeacherCourse

class CreateNewStudent(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class CreateNewTeacher(ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class CreateNewCourse(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CreateNewExam(ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'

class CreateNewTeacherCourse(ModelForm):
    class Meta:
        model = TeacherCourse
        fields = '__all__'