from django.contrib import admin
from .models import User,Project

class UsersAdmin(admin.ModelAdmin):
    pass

class ProjectsAdmin(admin.ModelAdmin):
    pass

admin.site.register(User, UsersAdmin)
admin.site.register(Project, ProjectsAdmin)
