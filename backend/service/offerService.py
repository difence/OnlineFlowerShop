import datetime
import json

import tool


def getOfferById(sqlClient: tool.sql.sqlClient, data):
    if 'id' in data:
        ids = data['id']
        res = {'code': 1, 'msg': '查询成功', 'data': toOutputDTO(sqlClient.searchInfo('offer_info', {'id': ids}))}
    else:
        res = {'code': 0, 'msg': 'id不存在', 'data': None}
    return json.dumps(res, ensure_ascii=False)


def getAll(sqlClient: tool.sql.sqlClient):
    sheet = sqlClient.searchInfo("offer_info", mult=True)
    result = []
    for i in range(len(sheet)):
        dt = toOutputDTO(sheet[i])
        result.append(dt)
    res = {"code": 1, "msg": "查找成功", "data": result}
    return json.dumps(res, ensure_ascii=False)


def updateById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": None, "msg": "修改成功"}
    ids = attrs['id']
    name = attrs["name"]
    msg = attrs["msg"]
    data = sqlClient.isExist("offer_info", {"id": ids})

    if data:
        sqlClient.update("offer_info", {"id": ids}, {'name': name, 'msg': msg,
                                                     'update_date': datetime.datetime.now().strftime(
                                                         "%Y-%m-%d %H:%M:%S")})
    else:
        res["code"] = 0
        res["msg"] = "供应商"
    return json.dumps(res, ensure_ascii=False)


def removeById(sqlClient: tool.sql.sqlClient, attrs: dict):
    data = sqlClient.isExist("offer_info", {"id": attrs['id']})
    if data:
        sqlClient.removeInfo('offer_info', attrs['id'])
    return json.dumps({"code": 1, "data": None, "msg": "删除成功"}, ensure_ascii=False)


def insert(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": '添加成功', "msg": None}

    sqlClient.insertInfo('offer_info',
                         {'id': tool.fun.getTimeStamp(),
                          'name': attrs['name'],
                          'msg': attrs['msg'],
                          'attachment_ids': attrs['attachment_ids'],
                          "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          "update_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sheet):
    res = {"id": sheet[0].replace(' ', ''),
           'name': sheet[1],
           'msg': sheet[2],
           'attachment_ids': sheet[3].split(','),
           "create_date": sheet[4].strftime("%Y-%m-%d %H:%M:%S"),
           "update_date": sheet[5].strftime("%Y-%m-%d %H:%M:%S")
           }
    return res
