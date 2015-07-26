from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from workspace.models import WorkSpace


def issue_config(req):
    WS = WorkSpace.objects.all()
    return render_to_response('issue_config.html', {'WS': WS})


def dummyissue(req):
    upid = req.REQUEST.get('id')
    upname = req.REQUEST.get('name')
    upsex = req.REQUEST.get('sex')
    upbirth = req.REQUEST.get('birth')
    uphighSchool = req.REQUEST.get('highSchool')
    upcollege = req.REQUEST.get('college')
    upqq = req.REQUEST.get('qq')
    upemail = req.REQUEST.get('email')
    upnote = req.REQUEST.get('note')
    oper = req.REQUEST.get('oper')
    if oper == 'del':
        WorkSpace.objects.filter(id=upid).delete()
    elif oper == 'edit' and upid == '0':
        p = WorkSpace(name=upname, sex=upsex, birth=upbirth, highSchool=uphighSchool, college=upcollege, qq=upqq,
                      email=upemail, note=upnote)
        p.save()
    else:
        WorkSpace.objects.filter(id=upid).update(name=upname, sex=upsex, birth=upbirth, college=upcollege,
                                                 highSchool=uphighSchool, qq=upqq, email=upemail, note=upnote)
    return HttpResponse(req)
