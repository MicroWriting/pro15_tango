from django.views import generic
from .models import Sentence, Tag
from django.shortcuts import render
from django.db.models import Q, Count
from braces.views import CsrfExemptMixin, JsonRequestResponseMixin
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt



class IndexView(generic.ListView):
    model = Sentence
    paginate_by = 10

'''
    def get_context_data(self):
        """テンプレートへ渡す辞書の作成"""
        context = super().get_context_data()
        #context['form'] = SearchForm(self.request.GET)   # 基の辞書に、formを追加
        return context
'''


class TagView(IndexView):
    def get_queryset(self):
        """タグで絞り込み"""
        tag_name = self.kwargs['tag']
        self.tag = Tag.objects.get(name=tag_name)
        queryset = super().get_queryset().filter(tag=self.tag)
        return queryset


class TagListView(generic.ListView):

    model = Tag
    queryset = Tag.objects.annotate(
        num_sentence=Count('sentence')).order_by('-num_sentence')

"""
class ModuleOrderView (CsrfExemptMixin, JsonRequestResponseMixin, View):
    def tag_order(self, request):
        for id, order in self.request_json.items():
"""


@csrf_exempt
def sort(request):
    for index, tag_pk in enumerate(request.POST.getlist('order-child[]')):
        tag = get_object_or_404(Tag, pk=tag_pk)
        tag.order = index
        tag.save()

    return HttpResponse('')