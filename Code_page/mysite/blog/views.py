from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


#El punto después de from indica el directorio actual o la aplicación actual.
#Como views.py y models.py están en el mismo directorio, simplemente usamos . y el
#nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post).

# Create your views here.
def post_list(request):
    if request.method == 'POST':
    	posts = reversed(Post.objects.filter(titulo__contains=request.POST.get('entrada')))
    else:
    	posts = reversed(Post.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion'))
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    if request.method == 'POST':
        posts = reversed(Post.objects.filter(titulo__contains=request.POST.get('entrada')))
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
