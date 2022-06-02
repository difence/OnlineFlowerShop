import datetime
import json

import backend.service.flowerService
import tool


def userInfo(mysqlClient: tool.sql.sqlClient, attrs: dict):
    sheet = mysqlClient.searchInfo("user_info", {"user_account": attrs["user_account"]}, mult=False)
    res = []
    for i in [sheet]:
        res.append({"user_id": i[0], "user_account": i[1], "user_password": i[2], "user_auth": i[3]})

    return json.dumps({"code": 1, "msg": "查找成功", "data": res[0]})


def getUserOrderById(sqlClient: tool.sql.sqlClient, attrs: dict):
    if 'user_id' in attrs:
        sheet = sqlClient.searchInfo("order_info", {"user_id": attrs["user_id"]}, mult=True)
    else:
        sheet = sqlClient.searchInfo("order_info", mult=True)
    result = []
    for i in range(len(sheet)):
        dt = toOutputDTO(sqlClient, sheet[i])
        result.append(dt)
    res = {"code": 1, "msg": "查找成功", "data": result}
    return json.dumps(res, ensure_ascii=False)


def updateOrderStatusById(sqlClient: tool.sql.sqlClient, data):
    sqlClient.update('order_info', attrs={'id': data['id']}, val={'status': data['status']})
    res = {"code": 1, "msg": "修改成功", "data": None}
    return json.dumps(res, ensure_ascii=False)


def getOrderById(sqlClient: tool.sql.sqlClient, data):
    if 'id' in data:
        ids = data['id']
        res = {'code': 1, 'msg': '查询成功',
               'data': toOutputDTO(sqlClient, sqlClient.searchInfo('order_info', {'id': ids}))}
    else:
        res = {'code': 0, 'msg': 'id不存在', 'data': None}
    return json.dumps(res, ensure_ascii=False)


def insert(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": '添加成功', "msg": None}

    sqlClient.insertInfo('order_info',
                         {'id': tool.fun.getTimeStamp(),
                          'user_id': attrs['user_id'],
                          'number': attrs['bucket'],
                          'bucket_id': attrs['bucket_id'],
                          "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          "status": 1})
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sqlClient: tool.sql.sqlClient, sheet):
    res = {"id": sheet[0].replace(" ", ""),
           "user_id": json.loads(backend.service.userService.getElemById(sqlClient, {"id": sheet[1].replace(" ", "")}))[
               'data'],
           "number": sheet[2],
           "bucket_id":
               json.loads(backend.service.flowerService.getElemById(sqlClient, {"id": sheet[3].replace(" ", "")}))[
                   "data"],
           "create_date": sheet[4].strftime("%Y-%m-%d %H:%M:%S"),
           "status": sheet[5]}
    return res
