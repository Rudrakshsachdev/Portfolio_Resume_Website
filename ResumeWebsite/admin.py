from django.contrib import admin
from .models import Project, ContactMessage, Experience

# Register your models here.

admin.site.register(Project) # registering the Project model to make it accessible in the admin interface
admin.site.register(ContactMessage) # registering the ContactMessage model to make it accessible in the admin interface
admin.site.register(Experience)
