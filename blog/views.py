from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.utils import timezone
from .models import Post, Comentario
from .forms import PostForm, ComentarioForm
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def post_list(request):
    posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')

    page = request.GET.get('page', 1)

    paginator = Paginator(posts, 1)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comentarios = Comentario.objects.filter( fk_post= post)
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()


    else:
        data = {'fk_post': post.id }
        form = ComentarioForm(initial=data)
    return render(request, 'blog/post_detail.html',{'post': post, 'form':form, 'comentarios': comentarios})
