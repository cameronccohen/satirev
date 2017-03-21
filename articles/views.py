from django.shortcuts import render

from django.http import HttpResponse
from .models import *


def index(request):

	# get posts in descending order by date
	posts = Article.objects.all().order_by('posted')[:10]
	data = { "recents" : posts }


	# now get the list of all sections
	sections = Section.objects.all()

	#for asection in sections:
		#section_name = str(asection.name)
		#article_in_section = Article.objects.where(Section = asection).latest('posted')
		#data['sections'][section_name] = article_in_section
	
	template_name = 'articles/index.html'
	return render(request, template_name, data)

def section(request, section_id):
	return "hello"

def article(request, slug):
	return "hello"

