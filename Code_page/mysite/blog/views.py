from django.shortcuts import render
from django.utils import timezone
from .models import Post
#El punto después de from indica el directorio actual o la aplicación actual.
#Como views.py y models.py están en el mismo directorio, simplemente usamos . y el
#nombre del archivo (sin .py). Ahora importamos el nombre del modelo (Post).

# Create your views here.
def post_list(request):
    if request.method == 'POST':
    	print (request.POST.get('entrada'))
    	posts = reversed(Post.objects.filter(titulo__contains=request.POST.get('entrada')))
    else:	
    	posts = reversed(Post.objects.filter(fecha_creacion__lte=timezone.now()).order_by('fecha_creacion'))
    return render(request, 'blog/post_list.html', {'posts': posts})


