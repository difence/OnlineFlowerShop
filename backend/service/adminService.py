import json

import tool


def userInfo(mysqlClient: tool.sql.sqlClient, attrs: dict):
    sheet = mysqlClient.searchInfo("user_info", {"user_account": attrs["user_account"]}, mult=False)
    res = []
    for i in [sheet]:
        res.append({"user_id": i[0], "user_account": i[1], "user_password": i[2], "user_auth": i[3]})

    return json.dumps({"code": 0, "msg": "查找成功", "data": res[0]})


def userFileInfo(mysqlClient: tool.sql.sqlClient, attrs: dict):
    sheet = mysqlClient.searchInfo("file_info", {"user_name": attrs["user_account"]}, mult=True)
    print(attrs)
    result = []
    for i in range(len(sheet)):
        dt = {"file_id": sheet[i][0],
              "file_name": sheet[i][1],
              "file_type": sheet[i][2],
              "file_auth": sheet[i][3],
              "create_date": sheet[i][4].strftime("%Y-%m-%d %H:%M:%S"),
              "user_name": sheet[i][5],
              "last_date": sheet[i][6].strftime("%Y-%m-%d %H:%M:%S")}
        result.append(dt)

    return json.dumps({"code": 0, "msg": "查找成功", "data": result})
