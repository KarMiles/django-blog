from django.shortcuts import render
from django.views import generic
from .models import Post

# Create your views here.

# New View Checklist:
# 1. Create the view code (below)
# 2. Create a template to render the view
# 3. Connect up URLs in the urls.py file
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
