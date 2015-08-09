# coding=utf-8
import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from gather.models import Gathering
from django.http import HttpResponse
from workspace.models import User_Group_Relation


@login_required(login_url='/accounts/login/')
def showGatherJoinInfo(req):
    return render_to_response('gather.html', {'username': req.user.username})


@login_required(login_url='/accounts/login/')
def getGatherJoinInfo(req):
    pageinfo = req.REQUEST
    cur_page = pageinfo.get('page')  # 表示请求的是第几页
    cur_rows = int(pageinfo.get('rows'))  # 表示每页显示行数
    # cur_search=pageinfo.get('_search')#表示搜索内容的请求
    cur_sidx = pageinfo.get('sidx')  # 表示排序的列名
    cur_sord = pageinfo.get('sord')  # 表示采用的排序方式
    # cur_nd=pageinfo.get('nd')#表示已经发送请求的次数的参数名称
    cur_records = int(cur_page) * int(cur_rows) - int(cur_rows)  # 表示页面已经显示的数据数

    sql = '''SELECT B.id ,A.name,A.phone,B.isjoin,B.reason FROM workspace_user_group_relation B ,workspace_userspace A
             WHERE B.group_id= (SELECT C.id FROM workspace_groupspace C,workspace_user_group_relation B
                                  WHERE B.user_id=2 AND C.id=B.group_id AND C.id=1)
                                  AND A.id=B.user_id
                                  ORDER BY %s %s ''' % (cur_sidx, cur_sord)
    userJoinStatus = User_Group_Relation.objects.raw(sql)
    # 数据库limit start,end 方式 和列表 list[start:end] 性能比较?
    response_data = userJoinStatus[cur_records:cur_records + cur_rows]

    json_data = {}
    viewdata = []
    records = len(list(userJoinStatus))
    totalPages = (records - 1) / cur_rows + 1
    for row in response_data:
        data = {}
        data['relationId'] = row.id
        data['userName'] = row.name
        data['phoneNumber'] = row.phone
        data['isJoin'] = row.isjoin
        data['reason'] = row.reason
        viewdata.append(data)
    json_data['total'] = totalPages  # 总页数
    json_data['page'] = cur_page  # 返回当前页号
    json_data['records'] = records  # 总记录数
    json_data['rows'] = viewdata  # 所有记录的值
    return HttpResponse(json.dumps(json_data))


@login_required(login_url='/accounts/login/')
def dummyGatherJoinInfo(req):
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
