from django.contrib import admin

from .models import *

admin.site.register(Professor)
admin.site.register(Student)
admin.site.register(Supervisor)
admin.site.register(Course)
admin.site.register(LearningProgram)
