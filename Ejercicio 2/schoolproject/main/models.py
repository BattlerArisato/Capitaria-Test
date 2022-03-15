from django.db import models

# Create your models here.
class Student(models.Model):
    ID_Student = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    ID_Teacher = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Course(models.Model):
    ID_Course = models.CharField(max_length=10)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class TeacherCourse(models.Model):
    ID_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    ID_Teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_Course

class Exam(models.Model):
    ID_Exam = models.CharField(max_length=10)
    ID_Student = models.ForeignKey(Student, on_delete=models.CASCADE)
    ID_Course = models.ForeignKey(Course, on_delete=models.CASCADE)
    Score = models.IntegerField()

    def __str__(self):
        return self.ID_Exam
