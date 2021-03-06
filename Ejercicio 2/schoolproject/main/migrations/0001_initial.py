# Generated by Django 4.0.3 on 2022-03-14 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Course', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Student', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Teacher', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TeacherCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('ID_Teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.teacher')),
            ],
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_Exam', models.CharField(max_length=10)),
                ('Score', models.IntegerField()),
                ('ID_Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.course')),
                ('ID_Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.student')),
            ],
        ),
    ]
