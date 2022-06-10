from flask import Flask, request

import backend.service
import config
import tool

app = Flask(__name__)

app.config['JSON_AS_ASCII'] = False

sqlClient = tool.sql.sqlClient(config.sqlIp,
                               config.sqlPort,
                               config.sqlDatabase,
                               config.sqlAccount,
                               config.sqlPassword)

minioClient = tool.mio.minioClient(config.minioIp,
                                   config.minioPort,
                                   config.minioAccount,
                                   config.minioPassword,
                                   config.minioBucket)

sqlClient.setConnection()
minioClient.setConnection()


@app.route('/user/login', methods=['POST', 'GET'])
def userLogin():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.login(sqlClient, data)
    return res


@app.route('/user/register', methods=['POST', 'GET'])
def userRegister():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.register(sqlClient, data)
    return res


@app.route('/user/forget', methods=['POST', 'GET'])
def userForget():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.forget(sqlClient, data)
    return res


@app.route('/user/getById', methods=['POST', 'GET'])
def userGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.getElemById(sqlClient, data)
    return res


@app.route('/user/getByAccount', methods=['POST', 'GET'])
def userGetByAccount():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.userService.getElemByAccount(sqlClient, data)
    return res


@app.route('/order/getUserOrderById', methods=['POST', 'GET'])
def orderGetUserOrderById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.orderService.getUserOrderById(sqlClient, data)
    return res


@app.route('/order/updateStatusById', methods=['POST', 'GET'])
def orderUpdateOrderStatusById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.orderService.updateOrderStatusById(sqlClient, data)
    return res


@app.route('/order/getOrderById', methods=['POST', 'GET'])
def orderGetOrderById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.orderService.getOrderById(sqlClient, data)
    return res


@app.route('/flower/getById', methods=['POST', 'GET'])
def flowerGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.getElemById(sqlClient, data)
    return res


@app.route('/flower/insert', methods=['POST', 'GET'])
def flowerInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.insert(sqlClient, data)
    return res


@app.route('/flower/updateNumberById', methods=['POST', 'GET'])
def flowerUpdateNumberById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.updateNumberById(sqlClient, data)
    return res


@app.route('/flower/updateAttsById', methods=['POST', 'GET'])
def flowerUpdateAttsById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.updateAttsById(sqlClient, data)
    return res


@app.route('/flower/getAll', methods=['POST', 'GET'])
def flowerGetAll():
    res = backend.service.flowerService.getAll(sqlClient)
    return res


@app.route('/flower/buy', methods=['POST', 'GET'])
def flowerBuy():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.flowerService.buy(sqlClient, data)
    return res


@app.route('/offer/getById', methods=['POST', 'GET'])
def offerGetById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.offerService.getOfferById(sqlClient, data)
    return res


@app.route('/offer/getAll', methods=['POST', 'GET'])
def offerGetAll():
    res = backend.service.offerService.getAll(sqlClient)
    return res


@app.route('/offer/updateById', methods=['POST', 'GET'])
def offerUpdateById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.offerService.updateById(sqlClient, data)
    return res


@app.route('/offer/removeById', methods=['POST', 'GET'])
def offerRemoveById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.offerService.removeById(sqlClient, data)
    return res


@app.route('/offer/insert', methods=['POST', 'GET'])
def offerInsert():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.offerService.insert(sqlClient, data)
    return res


@app.route('/file/downloadById', methods=['POST', 'GET'])
def fileDownloadById():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.fileService.download(minioClient, sqlClient, data)
    return res


@app.route('/file/upload', methods=['POST', 'GET'])
def fileUpload():
    if request.method == 'POST':
        data = request.values.to_dict()
    else:
        data = request.args.to_dict()
    res = backend.service.fileService.upload(minioClient, sqlClient, data)
    return res


def run():
    app.run(host=config.httpIp, port=config.httpPort, debug=False)


if __name__ == "__main__":
    run()
