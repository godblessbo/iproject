# coding=utf-8

from gather import gather_sql
from gather.models import Gathering
from workspace.models import User_Group_Relation, UserSpace


def getGatherInfo(param):
    login_id = param['login_id']
    param['user_id'] = UserSpace.objects.get(loginUser=login_id).id
    sql = gather_sql.getGatherInfoSQL(param)
    gatherInfo = Gathering.objects.raw(sql)
    viewdata = []
    records = 0
    for row in gatherInfo:
        data = {}
        data['id'] = row.id
        data['creator'] = row.creator
        data['name'] = row.name
        data['desp'] = row.desp
        data['notes'] = row.notes
        data['startTime'] = row.startTime
        data['endTime'] = row.endTime
        data['place'] = row.place
        data['eat'] = row.eat
        data['sleep'] = row.sleep
        data['budget'] = row.budget
        data['summary'] = row.summary
        viewdata.append(data)
        records += 1
    gather = {}
    gather['viewdata'] = viewdata
    gather['records'] = records
    return gather


def getGatherJoinInfo(pageinfo, param):
    # 用户自定义条件
    param['group_id'] = 1
    sql = gather_sql.getGatherJoinInfoSQL(param)
    # db = MySQLdb.connect(user='me', db='mydb', passwd='secret', host='localhost')
    # cursor = db.cursor()
    # cursor.execute('SELECT name FROM books ORDER BY name')
    # names = [row[0] for row in cursor.fetchall()]
    # db.close()
    userJoinStatus = User_Group_Relation.objects.raw(sql)
    viewdata = []
    records = 0
    for row in userJoinStatus:
        data = {}
        data['relationId'] = row.id
        data['userName'] = row.name
        data['phoneNumber'] = row.phone
        data['isJoin'] = row.isJoin
        data['reason'] = row.reason
        viewdata.append(data)
        records += 1
    joininfo = {}
    joininfo['viewdata'] = viewdata
    joininfo['records'] = records
    return joininfo
