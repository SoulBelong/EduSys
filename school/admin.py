from django.contrib import admin
from school import models

admin.site.register(models.Grade)
admin.site.register(models.Student)
admin.site.register(models.Teacher)
admin.site.register(models.User)
