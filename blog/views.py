from django.shortcuts import render
from blog.forms import CommentForm


# Import post & comment models
from blog.models import Post, Comment
# Create your views here.

# Creates Blog Index
def blog_index(request):
    # Get all posts & order them by the date they were created on
    posts = Post.objects.all().order_by('-created_on')
    # Set the context
    context = {
        "posts": posts,
    }
    return render(request, "blog_index.html", context)

# Creates Blog Category
def blog_category(request, category):
    # Uses Django queryset filter
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-created_on'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

# Creates blog details
# def blog_detail(request, pk):
#     # Get the post by the primary key
#     post = Post.objects.get(pk=pk)

#     # Create instance of our form class
#     form = CommentForm()
#     # Check if a post request has been received
#     if request.method == 'POST':
#         # Create a new instance of our form class populated w/ Post data
#         form.CommentForm(request.POST)
#         # Form is then validated
#         if form.is_valid():
#             # If its valid a new instance of comment is created
#             # Accessing data using form.cleaned_data which is a dictionary
#             comment = Comment(
#                 author=form.cleaned_data["author"],
#                 body=form.cleaned_data["body"],
#                 post=post,
#             )
#             # Save the comment to DB if it is valid & has been created
#             comment.save()
#     comments = Comment.objects.filter(post=post)      
#     context = {
#         "post": post,
#         "comments": comments,
#         "forms": form
#     }
#     return render(request, "blog_detail.html", context)


def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }
    return render(request, "blog_detail.html", context)