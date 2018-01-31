import os
import django
import csv
from django.template.defaultfilters import slugify
from django.core.files import File
import urllib

os.environ['DJANGO_SETTINGS_MODULE'] = 'satirev.settings'
django.setup()

from articles.models import *
from versatileimagefield.fields import VersatileImageField


tags = Tag.objects.all()
#print tags

Tag.objects.all().delete()
Image.objects.all().delete()
Article.objects.all().delete()


# with open("satirev-scraper/tags.csv","rb") as file:
#     reader = csv.reader(file)
#     for tag in reader:
#     	_, tag = Tag.objects.get_or_create(name=tag[1], slug=slugify(tag[1]))
#     	print tag

# with open("satirev-scraper/imageinfo.csv","rb") as file:
#     reader = csv.reader(file)
#     for image in reader:
#     	_, image = Image.objects.get_or_create(image=image[1], caption=image[2])

# tags = list(Tag.objects.all())
# sections = list(Section.objects.all())
# images = list(Image.objects.all())
# print tags

# with open("satirev-scraper/metadata.csv", "rb") as file:
# 	reader = csv.reader(file)
# 	for article in reader:
# 		tag = tags[int(article[4])]
# 		image = images[int(article[2])]
# 		section = sections[int(article[1])]

# 		print tag
# 		print image
# 		print section


with open("satirev-scraper/metadata.csv", "rb") as file:
	reader = csv.reader(file)
	for article in reader:
		art_img = article[2].split("    ")
		file_name = art_img[0]
		url = art_img[1]
		if url == "":
			url = "http://www.pixedelic.com/themes/geode/demo/wp-content/uploads/sites/4/2014/04/placeholder4.png"

		content = urllib.urlretrieve(url)
		image, _ = Image.objects.get_or_create(image=file_name, caption=art_img[2])

		image.image.save(file_name, File(open(content[0])))
		
		art_tags = article[4].split("    ")
		tags = []
		for x in art_tags:
			tag, _ = Tag.objects.get_or_create(name=x, slug=slugify(x))
			tags.append(tag)

		section = Section.objects.get(name=article[1])


		entry,_ = Article.objects.get_or_create(title=article[0],slug=slugify(article[0]),Section=section,image=image,body=article[3])
		for tag in tags:
			entry.tags.add(tag)


### shouldn't have modified metadata to put in the nums
#### just go through metadata, adding tags and images as you go, then use those objects to add the article itslef



# with open("satirev-scraper/metadata.csv",'rb') as file:
#     reader = csv.reader(file)
#     for article in reader:
#     	print article