from django.contrib import admin

# Register your models here.
from .models import User, Role, Directory, File

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Directory)
admin.site.register(File)