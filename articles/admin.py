from django.contrib import admin
from .models import *
from mce_filebrowser.admin import MCEFilebrowserAdmin

# Register your models here.

admin.site.register(Image)

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Tag, TagAdmin)
admin.site.register(Section, TagAdmin)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Article, ArticleAdmin)

