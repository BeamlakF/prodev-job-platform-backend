from django.contrib import admin
from .models import User, Category, Job, Application

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Job)
admin.site.register(Application)
