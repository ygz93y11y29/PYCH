# -*- coding: utf-8 -*-
##############################################################################
#                       myqr 生成二维码                                      #
##############################################################################
#pip3 install myqr
from MyQR import myqr
'''
可选参数	取值	解释
    -v	{1,2,3,...,40}	控制边长，范围是1至40，数字越大边长越大
    -l	{L,M,Q,H}	控制纠错水平，范围是L、M、Q、H，从左到右依次升高
    -n	output-filename	控制文件名，默认文件名是“ qrcode.png ",格式可以是 .jpg， .png ，.bmp ，.gif
    -d	output-directory	设置输出文件路径，而默认存储位置是当前目录
    -p	picture_file	引入图片，生成结合图片的二维码
    -c	不用取	可以使产生的图片由黑白变为彩色的
    -con	contrast	对比度，1.0 表示原始图片，更小的值表示更低对比度，更大反之。默认为1.0
    -bri	brightness	亮度，用法和取值与 -con 相同
'''

#------------------------------------------------------------------------------普通二维码
#生成普通的二维码
myqr.run("Hello World")
#通过指定save_name的内容修改生成的二维码文件名
myqr.run("Hello World", save_name="hello.jpg")

#------------------------------------------------------------------------------艺术二维码
"""
picture: 背景图的路径
colorized：是否需要着色，默认是False，不指定True，生成的为黑白二维码
"""
myqr.run('https://www.baidu.com/', picture='背景.jpg', colorized=True)
#或
myqr.run(
    words='http://www.baidu.com',    # 包含信息
    picture='lbxx.jpg',            # 背景图片
    colorized=True,            # 是否有颜色，如果为False则为黑白
    save_name='code.png'    # 输出文件名
)
#------------------------------------------------------------------------------动态二维码
myqr.run('https://www.baidu.com/', picture='动态背景.gif', colorized=True,
        save_name="动态qr.gif")



