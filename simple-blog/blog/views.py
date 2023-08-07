from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.shortcuts import redirect
from .models import Post
from .forms import CommentForm

#List of all posts
def post_list(request):
    posts = Post.objects.all()

    paginator = Paginator(posts, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'post/list.html', {'page_obj': page_obj})

#Detail view on post
# def post_detail(request, slug):
#     post = get_object_or_404(Post, slug=slug, status='published',)
#     return render(request,'post/detail.html', {'post': post})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    # List of active comments for this post
    comments = post.comments.filter(active=True)

    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
            return render(request, 'post/detail.html', {'post': post, 'comments': comments,  'comment_form': CommentForm()})
    if request.method == 'GET':
        comment_form = CommentForm()
    return render(request, 'post/detail.html', {'post': post, 'comments': comments,  'comment_form': comment_form})