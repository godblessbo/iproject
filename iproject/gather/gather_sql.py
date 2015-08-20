# coding=utf-8
def getGatherJoinInfoSQL(param):
    sql = '''SELECT E.*,A.name,A.phone
    FROM workspace_user_group_relation B,gather_joinstate E,workspace_userspace A
    WHERE A.id=B.user_id AND B.id=E.relation_key_id AND B.group_id=%s LIMIT %d,%d''' % (
        param['group_id'], param['startrecords'], param['endrecords'])
    return sql


def getGatherInfoSQL(param):
    sql = '''SELECT C.id,C.creator,C.name,D.desp,D.notes,D.startTime,D.endTime,D.place,D.eat,D.sleep,D.budget,D.summary
             FROM workspace_groupspace C ,gather_gathering D,(SELECT B.group_id FROM workspace_user_group_relation B WHERE B.user_id=%d) groups
             WHERE groups.group_id=C.id AND C.id=D.group_id ''' % param['user_id']
    return sql



