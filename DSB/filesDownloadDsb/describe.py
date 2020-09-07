# -*- coding: utf-8 -*-

##############################################################################
#                               下载文件                                      #
##############################################################################
import requests
def requestT():
    '''
        request  下载
    :return:
    '''
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596280388901&di=0703c65eafee0c7669225dba9fd488ec&imgtype=0&src=http%3A%2F%2Fh.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2Fc995d143ad4bd113cce8af145bafa40f4bfb05ea.jpg'
    myFile = requests.get(url)
    open('pythonImage', 'wb').write(myFile.content)

import wget
def wgetT():
    '''
        wget  下载
    :return:
    '''
    url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596281224663&di=79e69aa1c585a40dc9d8607724efc623&imgtype=0&src=http%3A%2F%2Fn.sinaimg.cn%2Fsinacn%2Fw480h679%2F20180217%2F6955-fyrpeif2262532.jpg'
    wget.download(url, 'pythonImage1')

import os
from time import time
from multiprocessing.pool import ThreadPool
def url_response(url):
    path, url = url
    r = requests.get(url)
    with open(path, 'wb') as f:
        for ch in r:
            f.write(ch)
urls = [('pythonImage2', 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596281224663&di=af3b043e8091f9c6302a630ecffd097e&imgtype=0&src=http%3A%2F%2Fwww.majiajia.cc%2Fdata%2Fattachment%2F2016-08%2F1b630786305563681c90807b657a692714065.jpg'),
            ('pythonImage3','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596281224662&di=9c13246943fcf91c888d20783d1ea96d&imgtype=0&src=http%3A%2F%2Fimg.18183.com%2Fuploads%2Fallimg%2F160301%2F27-160301155232.jpg'),
            ('pythonImage4','https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596282011795&di=ba7e95a360456ab88f89fe50510b8938&imgtype=0&src=http%3A%2F%2F01.minipic.eastday.com%2F20170519%2F20170519142625_de28e698821e86e712f064cde725d592_5.jpeg')]

def requestTD():
    start = time()
    for x in urls:
        url_response(x)

    print("time to download: ", time()-start)
    #0.19452857971191406

def requestTDB():
    start = time()
    ThreadPool(5).imap_unordered(url_response, urls)
    print("time to download: ", time()-start)


import asyncio
import urllib.request
import random

async def coroutine(url):
    r = urllib.request.urlopen(url)
    filename = "pythonImage{}".format(random.randint(6,20))
    with open(filename, 'wb') as f:
        for ch in r:
            f.write(ch)
    print_mag = "SuccessFull Download   "
    return print_mag

async def main_func(urls_to_download):
    co = [coroutine(url) for url in urls_to_download]
    downloaded, downloading = await asyncio.wait(co)
    for i in downloaded:
        print(i.result())

urls_to_download = ['https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596284239699&di=bddf2236e121d224c9fcfaf82d3a95c6&imgtype=0&src=http%3A%2F%2Fimg1.imgtn.bdimg.com%2Fit%2Fu%3D3122891051%2C868021368%26fm%3D214%26gp%3D0.jpg',
                    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596284301149&di=0b21a87a4a60b64f24b193373da24888&imgtype=0&src=http%3A%2F%2Fimg.pcauto.com.cn%2Fimages%2Fupload%2Fupc%2Ftx%2Fbbs6%2F1609%2F12%2Fc12%2F26852003_1473638112545_1024x1024.jpg',
                    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596284311586&di=581bca812b0c40f375ea8c2ba58faa6b&imgtype=0&src=http%3A%2F%2Fhbimg.b0.upaiyun.com%2F5b0751874f57187949bb29fc9cf1d21c8e4f72723c97b-VB2RTn_fw658',
                    'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1596284359194&di=38c3995ac3a621c4622dce0547ae3db4&imgtype=0&src=http%3A%2F%2Fimg.ewebweb.com%2Fuploads%2F20191220%2F12%2F1576814931-XKHBkiNQWO.jpg']

def asyncioD():
    '''
        异步下载：

            在这段代码中，我们创建了一个异步协同函数，它会下载我们的文件并返回一条消息。

            然后，我们使用另一个异步协同程序调用main_func，它会等待URL并将所有URL组成一个队列。asyncio的wait函数会等待协同程序完成。

            现在，为了启动协同程序，我们必须使用asyncio的get_event_loop()方法将协同程序放入事件循环中，最后，我们使用asyncio的run_until_complete()方法执行该事件循环。
            :return:
    '''
    eventLoop = asyncio.get_event_loop()
    eventLoop.run_until_complete(main_func(urls_to_download))











