from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UploadedFile(models.Model):
    name = models.CharField(default="File")
    description = models.TextField(default="")
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Comment(models.Model):
    creator = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadedFile, null=True, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

class FileUserPermission(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    file = models.ForeignKey(UploadedFile, null=True, on_delete=models.CASCADE)
    permit = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)