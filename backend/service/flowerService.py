import json

import backend.service.fileService
import tool


def getElemById(sqlClient: tool.sql.sqlClient, attrs: dict):
    res = {"code": 0, "data": None, "msg": None}
    sheet = sqlClient.searchInfo("flower_bucket", {"id": attrs["id"]})
    res['code'] = 1
    res['data'] = toOutputDTO(sqlClient, sheet)
    res['msg'] = '查找成功'
    return json.dumps(res, ensure_ascii=False)


def toOutputDTO(sqlClient: tool.sql.sqlClient, sheet):
    res = {"id": sheet[0].replace(" ", ""),
           "name": sheet[1],
           "color": sheet[2],
           "offer_id": sheet[3].replace(" ", ""),
           "bucket": sheet[4],
           "msg": sheet[5],
           "due_date": sheet[6].strftime("%Y-%m-%d %H:%M:%S"),
           "price": sheet[7],
           "attachment_ids":
               json.loads(backend.service.fileService.getElemById(sqlClient, {"id": sheet[8].replace(" ", "")}))[
                   "data"],
           "create_date": sheet[9].strftime("%Y-%m-%d %H:%M:%S"),
           "update_date": sheet[10].strftime("%Y-%m-%d %H:%M:%S")}
    return res
