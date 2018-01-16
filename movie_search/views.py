from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import movie_search.models as mm
from django.views.decorators.cache import cache_page
from testapp.models import Article

@cache_page(60 * 60 * 24)
def index(request):
    return render(request, 'movie_search/index.html')

@cache_page(60 * 60 * 24)
def search_result(request):
    search_title = request.POST.get('search-box')
    if search_title is None :
        return render(request, 'movie_search/index.html')

    search_result = mm.Movies.objects.filter(movie_title__contains=search_title)
    return render(request, 'movie_search/search_result.html',{'search_result': search_result, 'counts': len(search_result), 'search_title': search_title})

def ajax_list(request):
    a = range(100)
    return JsonResponse(list(a), safe=False)

def ajax_dict(request):
    name_dict = {'stefan': 'Love python and Django', 'rocky': 'I am teaching Django'}
    return JsonResponse(name_dict)

def ajax_test(request):
    return render(request, 'movie_search/ajax_test.html')

def home(request):
    return render(request, 'home_page.html', {'info': 'welcome to rocky\' site!'} )

class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView,self).get_context_data(**kwargs)
        context['latest_articles'] = Article.objects.all()[:5]
        return context


# Create your views here.
