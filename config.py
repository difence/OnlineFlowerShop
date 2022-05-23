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
minioBucket = 'editor'

userLoginUrl = '{}/{}'.format(httpUrl, 'user/login')
userRegisterUrl = '{}/{}'.format(httpUrl, 'user/register')
userForgetUrl = '{}/{}'.format(httpUrl, 'user/forget')
userGetByIdUrl = '{}/{}'.format(httpUrl, 'user/getById')
userGetByAccountUrl = '{}/{}'.format(httpUrl, 'user/getByAccount')

orderGetUserOrderById = '{}/{}'.format(httpUrl, 'order/getUserOrderById')

bucketGetById = '{}/{}'.format(httpUrl, 'flower/getById')
