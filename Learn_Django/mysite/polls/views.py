from django.http import Http404
from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from polls.models import Poll

from django.http import HttpResponse
# Create your views here.
def index(request):
    latest_poll_list = Poll.objects.order_by('-pub_date')[:5]
    context = {'latest_poll_list': latest_poll_list}
    return render(request, 'polls/index.html', context)
#    template = loader.get_template('polls/index.html')
#    context = RequestContext(request, {
#        'latest_poll_list': latest_poll_list,
#    })
#    return HttpResponse(template.render(context))
    #return HttpResponse("Hello, world. You're at the poll index.")

def detail(request, poll_id):
    try:
        poll = Poll.objects.get(pk=poll_id)
    except Poll.DoesNotExist:
        raise Http404
    return render(request, 'polls/detail.html', {'poll': poll})
    return HttpResponse("You're looking at the details of poll  %s." % poll_id)

def results(request, poll_id):
    return HttpResponse("You're looking at the results of poll %s." % poll_id)

def vote(request, poll_id):
    return HttpResponse("You're voting on poll %s." % poll_id)