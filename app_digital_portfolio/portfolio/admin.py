from django.contrib import admin
from .models import Project, ProjectSubtitle, BulletPoint

# Register your models here.
class ProjectAdmin(admin.ModelAdmin):
    pass
admin.site.register(Project, ProjectAdmin, BulletPoint)