from __future__ import unicode_literals

import os
from django.db import models
#import select2.fields


def upload_image_to(instance, filename):
    fname = ''.join([c for c in filename if c.isalnum() or c == '.'])
    return os.path.join('images', fname)

class Tag(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)

    def __unicode__(self):
        return self.name
    def get_absolute_url(self):
        # Can't use .format because name is not always
        return '/news/tag/' +  str(self.slug)

class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return self.name

class Image(models.Model):
    path = models.CharField(max_length=1000, blank=True)
    caption = models.TextField(max_length=10000, blank=True)
    slug = models.SlugField(max_length=100)
    def __unicode__(self):
        return str(self.id)
    def get_absolute_url(self):
        return "/media/" + path

        # Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=100)
    
    # PRODTODO have to make this rich text later

    body = models.TextField(max_length=10000, blank=True)
    # body = RedactorField(
    #     verbose_name=u'Text',
    #     redactor_options={'lang': 'en', 'focus': 'true'},
    #     upload_to='tmp/',
    #     allow_file_upload=True,
    #     allow_image_upload=True
    # )

    posted = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', related_name="category")

    #PRODTODO - add this in later
    #tags = select2.fields.ManyToManyField(Tag, blank=True, default = None)


    #posted = select2.fields.ManyToManyField(Category)
    #authors = select2.fields.ManyToManyField(Author, blank=True, default = None)

    first_image = models.ForeignKey(Image,null=True, blank=True, default = None)
    lead_photo = models.ImageField(upload_to=upload_image_to, blank=True, null=True)
    def __unicode__(self):
        return self.title
    def get_absolute_url(self):
        return '/ar/post/'+ self.slug
    def crop_first_image(self):
        return self.first_image
    def teaser(self):
        txt = re.sub("\{\{.*\}\}","",BeautifulSoup(self.body).text)
        i = 800
        while len(txt) > i and txt[i-1] != ".":
            i += 1
        if "(function" in txt:
            if txt.index("(function") < i:
                i = txt.index("(function") 
        return txt[:i]


