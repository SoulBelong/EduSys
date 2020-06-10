from django.shortcuts import render,HttpResponse,redirect
from django import views
from school import models

#登陆
class Login(views.View):
    def get(self,req):
        # ret = req.method
        return render(req,'login.html')

    def post(self,req):
            username = req.POST.get('username')
            pwd = req.POST.get('paw')
            userObj = models.User.objects.filter(name=username,password=pwd).first()
            if userObj:
                req.session['is_login']=True
                req.session['user']=username
                return redirect('/school/index/')
            else:
                return render(req,'login.html')
#注销
def logout(req):
    req.session.flush()
    return redirect('/school/login/')


#首页
def show(req):
    status = req.session.get('is_login')
    name = req.session.get('user')
    if status:
        return render(req,'index.html',{'user':name})
    else:
        return redirect('/school/login/')
#班级展示
def grade(req):
    status = req.session.get('is_login')
    name = req.session.get('user')
    if status:
        gradeObj = models.Grade.objects.all()
        return render(req,'grade.html',{'user':name,'data':gradeObj})
    else:
        return redirect('/school/login/')

def students(req):
    status = req.session.get('is_login')
    name = req.session.get('user')
    if status:
        studentsObj = models.Student.objects.all()
        return render(req,'students.html',{'data':studentsObj})
    else:
        return redirect('/school/login/')


def teachers(req):
    status = req.session.get('is_login')
    name = req.session.get('user')
    if status:
        teachersObj = models.Teacher.objects.all()
        return render(req,'teacher.html',{'data':teachersObj})
    else:
        return redirect('/school/login/')

