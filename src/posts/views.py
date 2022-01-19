from django.urls import reverse_lazy
from django.views.generic import DeleteView, ListView,DetailView, UpdateView, CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from posts.models import BlogPost

class BlogHome (ListView):
    model = BlogPost
    context_object_name = "posts"
    
    def get_queryset(self):
        queryset=super().get_queryset()
        if self.request.user.is_authenticated: #si on est connecté, on retourne tous les articles
            return queryset
        return queryset.filter(published=True)

class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'

class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = "posts/blogpost_edit.html"
    fields= fields = ["title", 'content', 'published']

@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "posts/blogpost_create.html"
    fields = ["title", 'content',]



class BlogPostDelete(DeleteView):
    model =BlogPost
    context_object_name = 'posts/blogpost_delete.html'
    success_url = reverse_lazy("posts:home")
# Create your views here.
