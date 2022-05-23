import datetime
import json

import tool


def login(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}
    if "account" not in attrs.keys():
        res["msg"] = "请求参数没有账号"
        return res
    if "password" not in attrs.keys():
        res["msg"] = "请求参数没有密码"
        return res
    account = attrs["account"]
    password = attrs["password"]
    data = sqlClient.isExist("user_info", {"account": account, "password": password})
    if data:
        ids = sqlClient.searchInfo("user_info", {"account": account})
        res["data"] = {"id": ids[0]}
        res["msg"] = "登录成功"
        res["code"] = 1
    else:
        res["msg"] = "账号或密码不存在"
    return json.dumps(res, ensure_ascii=False)


def register(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}

    if "account" not in attrs.keys():
        res["msg"] = "请求参数没有账号"
        return res

    if "password" not in attrs.keys():
        res["msg"] = "请求参数没有密码"
        return res

    account = attrs["account"]
    password = attrs["password"]
    tel = attrs["tel"]
    bir = attrs["birth"]

    data = sqlClient.isExist("user_info", {"account": account})

    if data:
        res["msg"] = "账号已存在"
    else:
        sqlClient.insertInfo("user_info",
                             {"id": tool.fun.getTimeStamp(),
                              "account": account,
                              "password": password,
                              "tel": tel,
                              "score": 0,
                              "score_sum": 0,
                              "birth": bir,
                              "create_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                              "update_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
        res["msg"] = "注册成功"
        res["code"] = 1
        res["data"] = {"auth": 0}
    return json.dumps(res, ensure_ascii=False)


def getElemByAccount(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}
    data = sqlClient.isExist("user_info", {"account": attrs["account"]})
    if data:
        sheet = sqlClient.searchInfo("user_info", {"account": attrs["account"]})
        s = {"id": sheet[0].replace("" "", ""),
             "account": sheet[1].replace("" "", ""),
             "password": sheet[2].replace("" "", ""),
             "tel": sheet[3].replace("" "", ""),
             "score": sheet[4],
             "score_sum": sheet[5],
             "birth": sheet[6].strftime("%Y-%m-%d %H:%M:%S")}
        res["data"] = s
        res["code"] = 1
        res["msg"] = "成功"
    else:
        res["msg"] = "找不到该用户"
    return json.dumps(res, ensure_ascii=False)


def getElemById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}
    data = sqlClient.isExist("user_info", {"id": attrs["id"]})
    if data:
        sheet = sqlClient.searchInfo("user_info", {"id": attrs["id"]})
        s = {"id": sheet[0].replace(" ", ""),
             "account": sheet[1].replace(" ", ""),
             "password": sheet[2].replace(" ", ""),
             "tel": sheet[3].replace(" ", ""),
             "score": sheet[4],
             "score_sum": sheet[5],
             "birth": sheet[6].strftime("%Y-%m-%d %H:%M:%S")}
        res["data"] = s
        res["code"] = 1
        res["msg"] = "成功"
    else:
        res["msg"] = "找不到该用户"
    return json.dumps(res, ensure_ascii=False)


def forget(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": None, "msg": "修改成功"}
    account = attrs["account"]
    password = attrs["password"]
    data = sqlClient.isExist("user_info", {"account": account})

    if data:
        sqlClient.update("user_info", {"account": account}, {"password": password})
    else:
        res["code"] = 0
        res["msg"] = "账号不存在"
    return json.dumps(res, ensure_ascii=False)
