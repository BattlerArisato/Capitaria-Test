from django.db.models import Avg
from django.shortcuts import render, redirect
from .models import Student, Course, Exam
from .forms import CreateNewExam, CreateNewStudent, CreateNewTeacher, CreateNewCourse, CreateNewTeacherCourse

# Create your views here.

def index(response):
    ls = Exam.objects.all()
    return render(response, 'main/index.html', {'ls': ls})

def newStudent(response):
    form = CreateNewStudent()
    if response.method == 'POST':
        form = CreateNewStudent(response.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    return render(response, 'main/newStudent.html', {'form': form})

def newTeacher(response):
    form = CreateNewTeacher()
    if response.method == 'POST':
        form = CreateNewTeacher(response.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    return render(response, 'main/newTeacher.html', {'form': form})

def newCourse(response):
    form = CreateNewCourse()
    if response.method == 'POST':
        form = CreateNewCourse(response.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    return render(response, 'main/newCourse.html', {'form': form})

def assignateTeacher(response):
    form = CreateNewTeacherCourse()
    if response.method == 'POST':
        form = CreateNewTeacherCourse(response.POST)
        if form.is_Valid:
            form.save()
            return redirect('index')
    
    return render(response, 'main/assignTeacher.html', {'form': form})

def newExam(response):
    form = CreateNewExam()
    if response.method == 'POST':
        form = CreateNewExam(response.POST)
        if form.is_valid:
            form.save()
            return redirect('index')

    return render(response, 'main/newExam.html', {'form': form})

def studentList(response):
    ls = Student.objects.all()
    return render(response, 'main/studentList.html', {'ls': ls})

def courseList(response):
    ls = Course.objects.all()
    return render(response, 'main/courseList.html', {'ls': ls})

def updateStudent(response, pk):
    student = Student.objects.get(id=pk)
    form = CreateNewStudent(instance=student)
    if response.method == 'POST':
        form = CreateNewStudent(response.POST, instance=student)
        if form.is_valid:
            form.save()
            return redirect('student-list')

    return render(response, 'main/updateStudent.html', {'form': form})

def deleteStudent(response, pk):
    student = Student.objects.get(id=pk)
    if response.method == 'POST':
        student.delete()
        return redirect('index')
    return render(response, 'main/deleteStudent.html', {'obj': student})

def updateCourse(response, pk):
    course = Course.objects.get(id=pk)
    form = CreateNewCourse(instance=course)
    if response.method == 'POST':
        form = CreateNewCourse(response.POST, instance=course)
        if form.is_valid:
            form.save()
            return redirect('index')

    return render(response, 'main/updateCourse.html', {'form': form})

def deleteCourse(response, pk):
    course = Course.objects.get(id=pk)
    if response.method == 'POST':
        course.delete()
        return redirect('index')
    return render(response, 'main/deleteCourse.html', {'obj': course})

def updateExam(response, pk):
    exam = Exam.objects.get(id=pk)
    form = CreateNewExam(instance=exam)
    if response.method == 'POST':
        form = CreateNewExam(response.POST, instance=exam)
        if form.is_valid:
            form.save()
            return redirect('index')
    
    return render(response, 'main/updateExam.html', {'form': form})

def deleteExam(response, pk):
    exam = Exam.objects.get(id=pk)
    if response.method == 'POST':
        exam.delete()
        return redirect('index')
    return render(response, 'main/deleteExam.html', {'obj': exam})

def studentInfo(response, pk):
    st = Student.objects.get(id=pk)
    info = Exam.objects.filter(ID_Student=pk).aggregate(Avg('Score'))
    return render(response, 'main/studentInfo.html', {'info': info, 'st': st})