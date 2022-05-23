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
    sheet = sqlClient.searchInfo("order_info", {"user_id": attrs["user_id"]}, mult=True)
    result = []
    for i in range(len(sheet)):
        dt = toOutputDTO(sqlClient, sheet[i])
        result.append(dt)
    res = {"code": 1, "msg": "查找成功", "data": result}
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sqlClient: tool.sql.sqlClient, sheet):
    res = {"id": sheet[0].replace(" ", ""),
           "user_id": json.loads(backend.service.userService.getElemById(sqlClient, {"id": sheet[1].replace(" ", "")}))[
               'data'],
           "number": sheet[2],
           "bucket_id":
               json.loads(backend.service.flowerService.getElemById(sqlClient, {"id": sheet[3].replace(" ", "")}))[
                   "data"],
           "create_date": sheet[4].strftime("%Y-%m-%d %H:%M:%S")}
    return res
