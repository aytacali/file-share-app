from django import forms
from .models import UploadedFile, Comment

class UploadFileForm(forms.ModelForm):
    friend = forms.CharField(help_text="If you want to send this file to your friend, write down her/his username or email.", required=False)
    comment_permission = forms.BooleanField(help_text="Comment permission", required=False)
    class Meta:
        model = UploadedFile
        fields = ('name', 'description', 'file',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)