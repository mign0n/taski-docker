"""Admin panel config."""

from django.contrib import admin

from .models import Task


class TaskAdmin(admin.ModelAdmin):
    """Task model customization."""

    list_display = ('title', 'description', 'completed')


admin.site.register(Task, TaskAdmin)
