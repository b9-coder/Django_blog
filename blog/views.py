from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.views import generic
from .forms import CommentForm, PostForm, ImageForm
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib.auth.models import User
from .forms import UserRegistrationForm

class PostList(generic.ListView):
    queryset = Post.objects.order_by('-created_on')
    template_name = 'index.html'
    context_object_name = 'data'
    paginate_by = 5

class PostRead(generic.DetailView):
    model = Post
    template_name = 'index_read.html'	

def news(request):
    return render(request, 'news.html')
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.for_post = post
            comment.save()
            return redirect('postRead', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'indexComment.html', {'form': form})



@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('postRead', pk=comment.for_post.pk)



@login_required
def post_remove(request, pk):
    Post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index', pk=post.pk)



@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_on = timezone.now()
            post.save()
            return redirect('postRead', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


def Log(request):
	redirect('/')

def Logout(request):
	pass



@login_required
def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            return render(request,'index.html', {'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'add_image.html', {'form': form})

# Create Post with image
@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            img_obj = form.instance
            image =  img_obj

            post.save()
            return redirect('postRead', pk=post.pk)
            
    else:
        form = PostForm()
    return render(request, 'post_edit.html', {'form': form})

def news(request):
    return render(request, 'news.html')

def about_blog(request):
    return render(request, 'about_blog.html')