from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


def index(request):

	# get posts in descending order by date
	posts = Post.objects.all().order_by('posted')[:10]
	data = { "recents" : posts }

	

    return render(request, 'articles/index.html')