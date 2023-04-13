from django.contrib import admin

# Import Models you want to register on admin page
from projects.models import Project
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass


# Register the models with the admin classes
admin.site.register(Project, ProjectAdmin)