from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from gather.models import Gathering


@login_required(login_url='/accounts/login/')
def dummyGatherInfo(req):
    upid = req.REQUEST.get('id')
    upcreator = req.REQUEST.get('creator')
    upmember = req.REQUEST.get('member')
    upplace = req.REQUEST.get('place')
    updesp = req.REQUEST.get('desp')
    upstartTime = req.REQUEST.get('startTime')
    upendTime = req.REQUEST.get('endTime')
    upnotes = req.REQUEST.get('notes')
    upeat = req.REQUEST.get('eat')
    upsleep = req.REQUEST.get('sleep')
    upbudget = req.REQUEST.get('budget')
    upnotes = req.REQUEST.get('notes')
    oper = req.REQUEST.get('oper')
    if oper == 'del':
        Gathering.objects.filter(id=upid).delete()
    elif oper == 'edit' and upid == '0':
        p = Gathering(creator=upcreator, member=upmember, desp=updesp, startTime=upstartTime, endTime=upendTime,
                      place=upplace, notes=upnotes)
        p.save()
    else:
        Gathering.objects.filter(id=upid).update(creator=upcreator, member=upmember, desp=updesp, startTime=upstartTime,
                                                 endTime=upendTime,
                                                 place=upplace, notes=upnotes)
    return HttpResponse(req)
