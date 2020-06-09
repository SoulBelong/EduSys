from django.db import models

class Grade(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=16)
    password = models.CharField(max_length=16,default='123456')
    age = models.SmallIntegerField()
    gender_choices = (
        (0,'男'),
        (1,'女'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    birth = models.DateField()
    telphone = models.CharField(max_length=16)
    addr = models.CharField(max_length=32)
    grade = models.ForeignKey(to='Grade',on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    password = models.CharField(max_length=16,default='123456')
    age = models.SmallIntegerField()
    gender_choices = (
        (0,'男'),
        (1,'女'),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    birth = models.DateField()
    tel = models.CharField(max_length=16)
    addr = models.CharField(max_length=32)
    grades = models.ManyToManyField(to='Grade')

    def __str__(self):
        return self.name

