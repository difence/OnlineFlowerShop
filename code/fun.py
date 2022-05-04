import datetime
import json
import logging
import sys
import time

import cv2
import matplotlib.pyplot as plt
import pandas as pd
import requests
from PIL import Image
from PIL import ImageTk

WARN = 0
INFO = 1
MESSAGE = 2
logging.StreamHandler(sys.stdout)
logging.getLogger().addHandler(logging.StreamHandler())
logging.getLogger().setLevel(logging.INFO)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


def logFormat(l, info):
    """
    将运行日志输出到控制台。
    1：INFO
    2：WARN
    3：MESSAGE
    :param l: 输出信息的等级
    :param info: 输出信息的语句
    :return: None
    """

    if l == 1:
        level = 'INFO'
    elif l == 2:
        level = 'WARN'
    else:
        level = 'MESSAGE'
    """
    此处可以调用fun.X，X就是需要输出的信息提示。
    """

    t = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    val = '[{}] {} {}'.format(level, t, info)
    """
    获取当前时间，将输出语句格式化。
    """

    logging.info(val)


def getTimeStamp() -> int:
    """
    获取时间戳，精确到毫秒。
    :return:返回时间戳
    """

    return int(time.time() * 1000)


def pic2TKpic(img, img_size):
    """
    用cv2的方法读取图像，转为array类型，再转为tk类型。
    普通的tk方法不能显示gif以外的图片。
    :param img: 图片路径。
    :param img_size: 图片大小（长*宽）。
    :return:
    """

    img_ = cv2.imread(img)
    """
    读取图片
    """

    img__ = cv2.resize(img_, img_size)
    """
    将图片变换为（长*宽）
    """

    img__ = cv2.cvtColor(img__, cv2.COLOR_BGR2RGB)
    """
    由于cv2读取的图像通道是BGR，需要将其转化为RGB，转为矩阵的颜色才会显示正常。
    """

    img___ = Image.fromarray(img__)
    """
    将cv2的矩阵转化为array格式。
    """

    img____ = ImageTk.PhotoImage(image=img___)
    """
    将array格式转化为ImageTk格式。
    """

    return img____


def getNeteaseSongList(name):
    """
    获取网易云音乐搜索接口。
    :param name: 搜索信息
    :return: 返回数据，type=DataFrame
    """

    url = 'http://music.cyrilstudio.top/search?keywords={}'
    url = url.format(name)
    """
    接口地址，将url格式化为需要搜索的内容
    """

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}
    """
    U-A请求头，没有此请求头将会被反爬。如果出现无法搜索，需要更换。
    """

    res = requests.get(url, headers=header)

    cont = res.content
    dec = cont.decode('utf-8')
    """
    获取数据，使用utf-8的编码格式解码
    """

    js = json.loads(dec)
    result = js['result']
    songs = result['songs']
    """
    把结果转化为json格式，提取需要的结果
    |
    +|data
    -+|result
    --+|songs
    """

    df = pd.DataFrame(data=songs)
    """
    将结果转化为DataFrame格式
    """

    return df


def getNeteaseSongListFormatAppends(df):
    """
    解析作者信息和作品集信息。
    :param df: DataFrame格式，必须输入函数 getNeteaseSongList 函数的输出
    :return: artistsSheet, albumSheet 分别是作者信息和作品信息
    """

    artists = df['artists']
    album = df['album']
    """
    提取信息。
    """

    artistsList = artists.values.tolist()
    albumList = album.values.tolist()
    """
    转化信息为list格式
    """

    artistsLists = []
    for i in artistsList:
        temp = i[0]
        artistsLists.append(temp)

    albumLists = []
    for i in albumList:
        temp = i
        albumLists.append(temp)
    """
    读取信息，获取歌手名和音乐集名
    """

    artistsSheet = pd.DataFrame(data=artistsLists)
    albumSheet = pd.DataFrame(data=albumLists)
    """
    转化为DataFrame格式
    """

    return artistsSheet, albumSheet


def getNeteaseSongMessages(ids):
    """
    获取网易云音乐的评论信息。
    :param ids: 歌曲的id号
    :return: resSheet list格式
    """

    url = 'http://music.cyrilstudio.top/comment/music?id={}&limit=1'
    urlFormat = url.format(ids)
    """
    接口地址，将url格式化为需要搜索的内容
    """

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

    res = requests.get(urlFormat, headers=header)

    cont = res.content
    dec = cont.decode('utf-8')

    js = json.loads(dec)
    hotComments = js['hotComments']
    comments = js['comments']
    """
    获取数据，使用utf-8的编码格式解码
    """

    resSheet = []
    for i in hotComments:
        commentFormat = '热评：{}'.format(i['content'])
        resSheet.append(commentFormat)
    for i in comments:
        commentFormat = '评论：{}'.format(i['content'])
        resSheet.append(commentFormat)
    """
    提取信息
    """

    return resSheet
