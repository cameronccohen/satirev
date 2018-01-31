from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):

	data = {}
	# get posts in descending order by date
	data["recents"] = Article.objects.all().order_by('-posted')[:10] 
	data["most_read"] = MostRead.objects.get()


	# now get the list of all sections
	sections = Section.objects.all()

	#for asection in sections:
		#section_name = str(asection.name)
		#article_in_section = Article.objects.where(Section = asection).latest('posted')
		#data['sections'][section_name] = article_in_section
	
	template_name = 'index.html'
	return render(request, template_name, data)

def section(request, section):

	data = {}
	print Article.objects.filter(Section__slug__iexact=section).order_by('-posted')[:10]
	# get posts in descending order by date
	data["recents"] = Article.objects.filter(Section__slug__iexact=section).order_by('-posted')[:10]
	data["most_read"] = MostRead.objects.get()

	template_name = 'section.html'
	return render(request, template_name, data)

def article(request, slug):

	data = {}

	data["article"] = Article.objects.get(slug__iexact=slug)
	data["most_read"] = MostRead.objects.get()

	template_name = 'article.html'
	return render(request, template_name, data)

def about(request):

	template_name = 'extra/about.html'
	return render(request,template_name)

def tag(request, tag):

	data = {}
	data["recents"] = Article.objects.filter(tags__slug=tag).order_by('-posted')[:10]
	data["tag"] = Tag.objects.get(slug__iexact=tag)

	template_name = 'tag.html'
	return render(request, template_name, data)


