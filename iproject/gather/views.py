# coding=utf-8
import json
from django.shortcuts import render_to_response, redirect
from dashboard.views import getusername
from gather.dummys import *
from gather.grids import *
from django.http import HttpResponse


def showPage(req):
    pagehtml = req.GET['pagehtml']
    username = getusername(req)
    if pagehtml == None or pagehtml == '':
        pagehtml = 'home.html'
    return render_to_response(pagehtml, {'username': username})


def getgrid(req):
    pageinfo = req.POST
    cur_page = int(pageinfo.get('page', 1))  # 表示请求的是第几页
    per_rows = int(pageinfo.get('rows', 15))  # 表示每页显示行数
    cur_search = pageinfo.get('_search')  # 表示搜索内容的请求
    login_id = req.user.id
    startrecords = (cur_page - 1) * per_rows  # 表示页面已经显示的数据数
    endrecords = startrecords + int(per_rows)
    param = {}
    griddata = {}
    param['startrecords'] = startrecords
    param['endrecords'] = endrecords
    param['cur_search'] = cur_search
    param['login_id'] = login_id
    grid = req.GET['grid']
    if grid == 'getGatherInfo':
        griddata = getGatherInfo(param)
    elif grid == 'getGatherJoinInfo':
        griddata = getGatherJoinInfo(pageinfo, param)
    viewdata = griddata['viewdata']
    records = griddata['records']
    json_data = {}
    totalPages = (records - 1) / per_rows + 1
    json_data['total'] = totalPages  # 总页数
    json_data['page'] = cur_page  # 返回当前页号
    json_data['records'] = records  # 总记录数
    json_data['rows'] = viewdata  # 所有记录的值
    return HttpResponse(json.dumps(json_data))


def dummygrid(req):
    grid = req.GET['grid']
    response_data = {}
    if grid == 'dummyGatherInfo':
        return dummyGatherInfo(req)
    else:
        response_data['message'] = 'can not find %s ,check editurl in your grid' % grid
        return HttpResponse(json.dumps(response_data))


def linkurl(req):
    linkinfo = str(req.GET['link']).split('?')
    arrivelink = linkinfo[0]
    rowid = linkinfo[1]
    if arrivelink == 'getGatherJoinInfo':
        nexturl = '/iproject/dashboard/showPage?pagehtml=' + 'join_info.html'
        return redirect(nexturl)
