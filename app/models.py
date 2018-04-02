from django.db import models
from django.utils import timezone


class Tag(models.Model):
    name = models.CharField('Tagname', max_length=255)
    created_at = models.DateTimeField('date', default=timezone.now)
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ordering', 'pk']


class Sentence(models.Model):
    name = models.TextField('Sentence')
    tag = models.ManyToManyField(Tag, verbose_name='tag')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']