
from django.http import HttpResponse
from django.shortcuts import render_to_response
from issue.models import Task
import json




def home(req):
    return render_to_response('home.html')
def issue(req):
    task = Task.objects.all()
    creators = Task.objects.raw('select id ,creator from issue_task')
    return render_to_response('issue.html',{'task': task, 'creators': creators})

def settings(req):
    return render_to_response('settings.html')


def dummy(req):
    upid = req.REQUEST.get('id')
    upcreator = req.REQUEST.get('creator')
    upowner = req.REQUEST.get('owner')
    uptask = req.REQUEST.get('task')
    Task.objects.filter(id=upid).update(creator=upcreator, owner=upowner, task=uptask)
    return HttpResponse(req)


def getselect(req):
    result = 'a'
    return HttpResponse(json.dumps(result))
