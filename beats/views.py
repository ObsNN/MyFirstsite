from django.shortcuts import render
from .models import Music
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def music(request):
	posts = Music.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'beats/music.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Music, pk=pk)
    return render(request, 'beats/post_detail.html', {'post': post})
