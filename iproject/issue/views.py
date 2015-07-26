from django.http import HttpResponse
from django.shortcuts import render_to_response
from issue.models import Task
from workspace.models import WorkSpace
import json


def issue(req):
    task = Task.objects.all()
    owners = task.values('owner')
    return render_to_response('issue.html', {'task': task, 'owners': owners})




def dummy(req):
    upid = req.REQUEST.get('id')
    upcreator = req.REQUEST.get('creator')
    upowner = req.REQUEST.get('owner')
    uptask = req.REQUEST.get('task')
    upprocess = req.REQUEST.get('process')
    upstartTime = req.REQUEST.get('startTime')
    upendTime = req.REQUEST.get('endTime')
    upstate = req.REQUEST.get('state')
    oper = req.REQUEST.get('oper')
    if oper == 'del':
        Task.objects.filter(id=upid).delete()
    elif oper == 'edit' and upid == '0':
        p = Task(creator=upcreator, owner=upowner, task=uptask, startTime=upstartTime, endTime=upendTime)
        p.save()
    else:
        Task.objects.filter(id=upid).update(creator=upcreator, owner=upowner, task=uptask, startTime=upstartTime,
                                            endTime=upendTime, process=upprocess, state=upstate)
    return HttpResponse(req)

#
# def getselect(req):
#     select = req.REQUEST.get('creator')
#     result = Task.objects.filter(creator=select).values('owner', 'task')[0]
#     return HttpResponse(json.dumps(result['owner']))
