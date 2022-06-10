httpIp = '127.0.0.1'
httpPort = '5000'
httpUrl = 'http://{}:{}'.format(httpIp, httpPort)

sqlIp = '127.0.0.1'
sqlPort = '233'
sqlAccount = 'flower'
sqlPassword = 'admin'
sqlDatabase = 'flower'

minioIp = '47.100.93.63'
minioPort = '9090'
minioAccount = 'admin'
minioPassword = 'admin123456'
minioBucket = 'flower'

userLoginUrl = '{}/{}'.format(httpUrl, 'user/login')
userRegisterUrl = '{}/{}'.format(httpUrl, 'user/register')
userForgetUrl = '{}/{}'.format(httpUrl, 'user/forget')
userGetByIdUrl = '{}/{}'.format(httpUrl, 'user/getById')
userGetByAccountUrl = '{}/{}'.format(httpUrl, 'user/getByAccount')

orderGetUserOrderById = '{}/{}'.format(httpUrl, 'order/getUserOrderById')
orderUpdateStatusById = '{}/{}'.format(httpUrl, 'order/updateStatusById')
orderGetOrderById = '{}/{}'.format(httpUrl, 'order/getOrderById')

offerGetById = '{}/{}'.format(httpUrl, 'offer/getById')
offerGetAll = '{}/{}'.format(httpUrl, 'offer/getAll')
offerUpdateById = '{}/{}'.format(httpUrl, 'offer/updateById')
offerRemoveById = '{}/{}'.format(httpUrl, 'offer/removeById')
offerInsert = '{}/{}'.format(httpUrl, 'offer/insert')

flowerGetById = '{}/{}'.format(httpUrl, 'flower/getById')
flowerGetAll = '{}/{}'.format(httpUrl, 'flower/getAll')
flowerInsert = '{}/{}'.format(httpUrl, 'flower/insert')
flowerUpdateNumberById = '{}/{}'.format(httpUrl, 'flower/updateNumberById')
flowerBuy = '{}/{}'.format(httpUrl, 'flower/buy')
flowerUpdateAttsById = '{}/{}'.format(httpUrl, 'flower/updateAttsById')

fileDownloadById = '{}/{}'.format(httpUrl, 'file/downloadById')
fileUpload = '{}/{}'.format(httpUrl, 'file/upload')
