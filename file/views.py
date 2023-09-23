from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import UploadedFile, Comment, FileUserPermission
from .forms import UploadFileForm, CommentForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

@login_required(login_url='/user/login')
def home_view(request):
	return render (request=request, template_name="home.html", context={})

@login_required(login_url="/user/login")
def upload_file(request):
    all_files = []
    # UploadedFile.objects.all().delete()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)

        if form.is_valid():
            form.instance.creator = request.user
            if form.data['friend']:
                user_exists = User.objects.filter(Q(username=form.data['friend']) | Q(email=form.data['friend']))[0]
                if not user_exists:
                    messages.error(request, "This user does not exists") #FLAW not user existence is still returning error. 
                    return redirect('login')
                
                uploaded_file = form.save()

                file_user = FileUserPermission(user=user_exists, file=uploaded_file, permit=True)
                file_user.save()            

            return redirect('/upload') #FLAW (look at the url names problem later)
    else:
        form = UploadFileForm()
    
    creator_files = UploadedFile.objects.filter(creator=request.user)
    friend_permits = FileUserPermission.objects.filter(user=request.user)

    for friend_permit in friend_permits:
        one_file = UploadedFile.objects.get(id=friend_permit.file.id)
        all_files.append(one_file)

    new_all_files = list(creator_files) + list(all_files)
    return render(request, 'upload_file.html', {'form': form, 'files': new_all_files})

@login_required(login_url="/user/login")
def download_file(request, file_id):

    uploaded_file = UploadedFile.objects.get(pk=file_id)
    response = HttpResponse(uploaded_file.file, content_type='application/force-download')

    response['Content-Disposition'] = f'attachment; filename="{uploaded_file.file.name}"'
    return response

@login_required(login_url="/user/login")
def file_detail_view(request, id = None):
    file = get_object_or_404(UploadedFile, id = id)

    if request.method == 'POST':
        form = CommentForm(request.POST)

        if form.is_valid():
            
            form.instance.creator = request.user
            form.instance.file = file

            form.save()
            return HttpResponseRedirect('/file/%d/'%id)
    else:
        form = CommentForm()

    comments = Comment.objects.all()
    return render(request, 'file_detail.html', {'file': file, 'form': form, 'comments': comments})
