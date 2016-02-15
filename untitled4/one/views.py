from django.shortcuts import  get_list_or_404
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from django.views import generic
from .models import Player, Game

# Create your views here.
def test(request):
    context=RequestContext(request,{})
    return render(request,'one/test.html', context)
def about(request):
    return render(request, 'one/about.html')
class IndexView(generic.ListView):
    template_name = 'one/index.html'
    #context_object_name = 'some_players'

    def get_queryset(self):
        return Player.objects.order_by('-total_games')[:10]

#def index(request):
#    players=Player.objects.order_by('name')
#    #template = loader.get_template('one/index.html')
#    context = RequestContext(request, {
#        'players': players,
#        })
#    #return HttpResponse(template.render(context))
#    return render(request,'one/index.html', context)

def predict(request):
    #games=Game.objects.filter(time=player_name)
    context = RequestContext(request, {})
    #print (player_name)
    return render(request,'one/predictions.html',context)
def strategy (request):
    context=RequestContext(request,{})
    return render(request,'one/strategy.html', context)

def predictSearch(request):
    if 'SearchByName' in request.GET:
        name=request.GET['SearchByName']
        message="Имя:   %r" % name
        player=Player.objects.filter(name=name)
        print ("Success")
    else:
        message="Провал"
        print ("Fail")
        player='Not found'
    #return HttpResponse(message)
    context=RequestContext(request, {'player': player,})
    return render(request,'one/SearchByName.html', context)
def variants(request):
    return render(request, 'one/variants.html')
def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)