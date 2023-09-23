from django.contrib import admin
from .views import UploadedFile, Comment, FileUserPermission

# Register your models here.
admin.site.register(UploadedFile)
admin.site.register(Comment)
admin.site.register(FileUserPermission)


