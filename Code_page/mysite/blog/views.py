from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect


#El punto después de from indica el directorio actual o la aplicación actual.
#Como views.py y models.py están en el mismo directorio, simplemente usamos . y el
#nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post).

# Create your views here.
def post_list(request):
    if request.method == 'POST':
        if request.POST.get('tag1')=='calculo':
          posts = reversed(Post.objects.filter(titulo__contains='calculo'))
        elif request.POST.get('tag2')=='ada':
          posts = reversed(Post.objects.filter(titulo__contains='ada'))
        elif request.POST.get('tag3')=='estadistica':
          posts = reversed(Post.objects.filter(titulo__contains='estadistica'))
        elif request.POST.get('tag4')=='libro':
          posts = reversed(Post.objects.filter(titulo__contains='libro'))
        elif request.POST.get('tag5')=='computacion grafica':
          posts = reversed(Post.objects.filter(titulo__contains='computacion grafica'))
        else:
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
        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                #post.autor = request.user
                post.fecha_creacion = timezone.now()
                post.save()
                return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})
