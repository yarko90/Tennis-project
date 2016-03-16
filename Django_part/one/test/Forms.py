__author__ = 'например Андрей'
from django import forms
from django.views import generic
class index_view(generic.ListView):
    template_name = 'one/index.html'
    # context_object_name = 'some_players'

    def get_queryset(self):
        return Player.objects.order_by('-total_games')[:10]


# def index(request):
#    players=Player.objects.order_by('name')
#    #template = loader.get_template('one/index.html')
#    context = RequestContext(request, {
#        'players': players,
#        })
#    #return HttpResponse(template.render(context))
#    return render(request,'one/index.html', context)
class predict_view(generic.ListView):
    template_name = 'one/predictions.html'
    context_object_name = 'game_list'

    def get_queryset(self):
        return Game.objects.order_by('-time')
