from django.shortcuts import render
from .models import Music
from django.utils import timezone

def music(request):
	posts = Music.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'beats/music.html', {'posts': posts})
