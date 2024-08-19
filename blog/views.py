from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy
from .forms import ImageForm

class BlogListView(ListView):
    model = Blog
    #context_object_name = 'imagens'

class BlogCreateView(CreateView):
    model = Blog
    fields = ["title", "description", "phtoto"]
    success_url = reverse_lazy('blog_list')

class ImageUpdateView(UpdateView):
    model = Blog
    form_class = ImageForm
    template_name = 'blog/blog_form.html'
    success_url = reverse_lazy('blog_list')
    
class ImageDeleteView(DeleteView):
    model = Blog
    template_name = 'blog/image_confirm_delete.html'
    success_url = reverse_lazy('blog_list')