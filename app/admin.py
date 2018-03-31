from django.contrib import admin
from .models import Sentence, Tag


class Sentenceadmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'get_tags')

    def get_tags(self, Sentence):
        tags = []
        for tag in Sentence.tag.all():
            tags.append(str(tag))
        return ', '.join(tags)


admin.site.register(Sentence,Sentenceadmin)


class TagAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)


admin.site.register(Tag, TagAdmin)