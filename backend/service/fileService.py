import datetime
import json

import backend.service.userService
import tool


def upload(minioClient: tool.mio.minioClient, mysqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}

    sheet = {"id": tool.fun.getTimeStamp(),
             "update_id": attrs["update_id"],
             "update_date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
             "name": attrs["name"],
             "type": attrs["type"],
             "tname": attrs["tname"]}
    mysqlClient.insertInfo("file_info", sheet)

    url = minioClient.uploadFile(sheet["id"], sheet["type"])
    res["data"] = {"url": url, "id": sheet["id"]}
    res["code"] = 1
    return json.dumps(res, ensure_ascii=False)


def download(minioClient: tool.mio.minioClient, sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}
    data = json.loads(getElemById(sqlClient, {"id": attrs["id"]}))["data"]
    url = minioClient.downloadFile(data["id"], data["type"])
    res["data"] = {"url": url, "data": data}
    res["code"] = 1
    return json.dumps(res, ensure_ascii=False)


def getElemById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 1, "data": None, "msg": None}
    sheet = sqlClient.searchInfo("file_info", {"id": attrs["id"]})
    sheet = toOutputDTO(sqlClient, sheet)
    res["data"] = sheet
    res["msg"] = "查找成功"
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sqlClient: tool.sql.sqlClient, sheet):
    res = {"id": sheet[0].replace(" ", ""),
           "name": sheet[1].replace(" ", ""),
           "type": sheet[2].replace(" ", ""),
           "tname": sheet[3].replace(" ", ""),
           "update_id":
               json.loads(backend.service.userService.getElemById(sqlClient, {"id": sheet[4].replace(" ", "")}))[
                   "data"],
           "update_date": sheet[5].strftime("%Y-%m-%d %H:%M:%S")}
    return res
