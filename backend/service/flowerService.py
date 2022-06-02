import datetime
import json
import pprint

import backend.service.fileService
import tool


def getElemById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": None, "msg": '查找成功'}
    sheet = sqlClient.searchInfo("flower_bucket", {"id": attrs["id"]})
    res['data'] = toOutputDTO(sheet)
    return json.dumps(res, ensure_ascii=False)


def getAll(sqlClient: tool.sql.sqlClient):
    sheet = sqlClient.searchInfo("flower_bucket", mult=True)
    result = []
    for i in range(len(sheet)):
        dt = toOutputDTO(sheet[i])
        result.append(dt)
    res = {"code": 1, "msg": "查找成功", "data": result}
    return json.dumps(res, ensure_ascii=False)


def buy(sqlClient: tool.sql.sqlClient, attrs: dict):
    ids = attrs['id']
    number = int(attrs['bucket'])
    user_id = attrs['user_id']

    sheet = sqlClient.isExist('flower_bucket', {'id': ids})
    if sheet:
        sheet = sqlClient.searchInfo('flower_bucket', {'id': ids})
        data = toOutputDTO(sheet)
        pprint.pprint(data)
    else:
        return json.dumps({"code": 0, "data": None, "msg": '花卉不存在'}, ensure_ascii=False)

    if int(data['bucket']) - number >= 0:
        sqlClient.update('flower_bucket', {'id': ids}, {'bucket': int(data['bucket']) - number})
        backend.service.orderService.insert(sqlClient, {'user_id': user_id, 'bucket': number, 'bucket_id': ids})
        return json.dumps({"code": 1, "data": None, "msg": '购买成功'}, ensure_ascii=False)
    else:
        return json.dumps({"code": 0, "data": {'bucket': data['bucket']}, "msg": '数量不足'}, ensure_ascii=False)


def insert(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": '添加成功', "msg": None}

    sqlClient.insertInfo('flower_bucket',
                         {'id': tool.fun.getTimeStamp(),
                          'name': attrs['name'],
                          'color': attrs['color'],
                          'offer_id': attrs['offer_id'],
                          'bucket': attrs['bucket'],
                          'msg': attrs['msg'],
                          'due_date': attrs['due_date'],
                          'price': attrs['price'],
                          'attachment_ids': attrs['attachment_ids'],
                          "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                          "update_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    return json.dumps(res, ensure_ascii=False)


def updateNumberById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": '添加成功', "msg": None}
    sqlClient.update('flower_bucket', {'id': attrs['id']}, {'bucket': attrs['bucket']})
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sheet):
    res = {"id": sheet[0].replace(" ", ""),
           "name": sheet[1],
           "color": sheet[2],
           "offer_id": sheet[3].replace(" ", ""),
           "bucket": sheet[4],
           "msg": sheet[5],
           "due_date": sheet[6].strftime("%Y-%m-%d %H:%M:%S"),
           "price": sheet[7],
           "attachment_ids": sheet[8].split(','),
           "create_date": sheet[9].strftime("%Y-%m-%d %H:%M:%S"),
           "update_date": sheet[10].strftime("%Y-%m-%d %H:%M:%S")}
    return res
