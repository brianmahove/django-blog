from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q
from .models import Post, Category, Comment
from .forms import CommentForm, PostForm

def post_list(request):
    posts_list = Post.objects.filter(status='published')
    
    # Search functionality
    query = request.GET.get('q')
    if query:
        posts_list = posts_list.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) |
            Q(excerpt__icontains=query)
        )
    
    # Category filter
    category_slug = request.GET.get('category')
    if category_slug:
        posts_list = posts_list.filter(categories__name=category_slug)
    
    paginator = Paginator(posts_list, 6)  # 6 posts per page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    
    categories = Category.objects.all()
    
    context = {
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'blog/post_list.html', context)

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, status='published')
    comments = post.comments.filter(approved=True)
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.author = request.user
            new_comment.save()
            messages.success(request, 'Your comment has been submitted and is awaiting approval.')
            return redirect('post_detail', slug=post.slug)
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'comment_form': comment_form,
    }
    return render(request, 'blog/post_detail.html', context)



@login_required
def create_post(request):
    categories = Category.objects.all()  # Get all categories
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()
            form.save_m2m()  # Save many-to-many data
            messages.success(request, 'Post created successfully!')
            return redirect('my_posts')  # Redirect to my_posts instead of post_list
    else:
        form = PostForm()
    
    return render(request, 'blog/create_post.html', {
        'form': form,
        'categories': categories
    })

@login_required
def my_posts(request):
    posts = Post.objects.filter(author=request.user)
    return render(request, 'blog/my_posts.html', {'posts': posts})