# -*- coding: utf-8 -*-
##############################################################################
#                        os 模块                                             #
##############################################################################
#加载
import os
#查看os下的函数
print("os:  ", dir(os))
#查看os.path下的函数
print("os.path: ", dir(os.path))

#-----------------------------------------------------------------------------os.name
'''
    描述：显示当前使用的平台，'nt'表示Windows，'posix' 表示Linux
    语法：os.name
'''
print("os.name: ", os.name)

#-----------------------------------------------------------------------------os.getcwd（）
'''
    描述：返回当前进程的工作目录。
    语法：os.getcwd()
'''
print("os.getcwd(): ", os.getcwd())

#-----------------------------------------------------------------------------os.chdir（）
'''
    描述：改变当前工作目录到指定的路径。
    语法：os.chdir(path)
'''
print("os.chdir前:    ", os.getcwd())
os.chdir(r'D:\CompleteProgram\canKaoFiles\needsFiles')
#再次查看当前目录，已经变成新的了
print("os.chdir后:    ", os.getcwd())
os.chdir(r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb')
#-----------------------------------------------------------------------------os.makedirs（）
'''
    描述：方法用于递归创建目录。像 mkdir(), 但创建的所有intermediate-level文件夹需要包含子目录。
    语法：os.makedirs(path, mode=0o777)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
if os.path.exists(path) == False:
    os.makedirs(r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log', mode=0o777)

#-----------------------------------------------------------------------------os.mkdir（）
'''
    描述：以数字权限模式创建目录。默认的模式为 0777 (八进制)。
    语法：os.mkdir(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log1'
if os.path.exists(path) == False:
    os.mkdir(path)

#-----------------------------------------------------------------------------os.listdir（）
'''
    描述：列出目录下的所有文件和文件夹
    语法：os.listdir（path）
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles'

print("os.listdir:  ", os.listdir(path))
print("os.listdir:  ", os.listdir('.'))

#-----------------------------------------------------------------------------os.remove（）
'''
    描述：用于删除指定路径的文件。如果指定的路径是一个目录，将抛出OSError。
    语法：os.remove(path)
'''
try:
    path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log1\python1.py'
    os.remove(path)
except Exception as error:
    print('已删除：',error)

#-----------------------------------------------------------------------------os.rename（）
'''
    描述：命名文件或目录,能对相应的文件进行重命名, 直接串path也可行
    语法：os.rename(src, dst)
        参数：src -- 要修改的目录名       dst -- 修改后的目录名
            
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log.log'
path1 = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log1.log'
# path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log1'
# path1 = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log2'
if os.path.exists(path) == True:
    os.rename(path, path1)

#-----------------------------------------------------------------------------os.renames()
'''
    描述：用于递归重命名目录或文件。类似rename()。既可以重命名文件, 也可以重命名文件的上级目录名
    语法：os.renames(old, new)
        参数：old -- 要重命名的目录   new --文件或目录的新名字。甚至可以是包含在目录中的文件，或者完整的目录树。
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log.log'
path1 = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log1.log'
# path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log1'
# path1 = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log2'
#文件夹和文件同时命名
print("os.renames前:", os.listdir(r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'))
os.renames(path1, path)
print("os.renames后:", os.listdir(r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'))

#-----------------------------------------------------------------------------os.linesep
'''
描述：当前平台用于分隔（或终止）行的字符串。它可以是单个字符，如 POSIX 上是 '\n'，也可以是多个字符，如 Windows 上是 '\r\n'。在写入以文本模式（默认模式）打开的文件时，请不要使用 os.linesep 作为行终止符，请在所有平台上都使用一个 '\n' 代替。
语法：os.linesep
'''
print("os.linesep:  ", os.linesep)

#-----------------------------------------------------------------------------os.pathsep
'''
    描述：操作系统通常用于分隔搜索路径（如 PATH）中不同部分的字符，如 POSIX 上是 ':'，Windows 上是 ';'。在 os.path 中也可用。
    语法：os.pathsep
'''
print("os.pathsep:  ", os.pathsep)

#-----------------------------------------------------------------------------os.close（）
'''
    描述：关闭指定的文件描述符 fd
    语法：os.close(fd)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log.log'
fd = os.open( path, os.O_RDWR|os.O_CREAT )
os.write(fd, bytes("This is test", encoding = "utf8"))
os.close( fd )

#-----------------------------------------------------------------------------os.stat（）
'''
    描述：获取文件或者目录信息
    语法：os.stat(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log.log'
print("os.stat: ", os.stat(path))

#-----------------------------------------------------------------------------os.sep()
'''
    描述：显示当前平台下路径分隔符,在 POSIX 上是 '/'，在 Windows 上是是 '\\'
    语法：os.sep
'''
print("os.sep: ", os.sep)
#-----------------------------------------------------------------------------os.path.abspath()
'''
    描述：返回文件的绝对路径
    语法：os.path.abspath(path)
'''
fileName = 'os_describe.py'
print("os.path.abspath: ", os.path.abspath(fileName))

#-----------------------------------------------------------------------------os.path.basename()
'''
    描述：返回文件名，纯粹字符串处理逻辑，路径错误也可以
    语法：os.path.basename(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log\log.log'
print("os.path.basename:    ",(path))

#-----------------------------------------------------------------------------os.path.commonprefix()
'''
    描述：返回list(多个路径)中，所有path共有的最长的路径
    语法：os.path.commonprefix(list)
'''
print("os.path.commonprefix: ", os.path.commonprefix(['http://c.biancheng.net/python/aaa', 'http://c.biancheng.net/shell/']))
print("os.path.commonprefix: ", os.path.commonprefix(['http://bianc/python/aaa', 'http://c.biancheng.net/shell/']))

#-----------------------------------------------------------------------------os.path.dirname()
'''
    描述：返回文件路径
    语法：os.path.dirname(path)
'''
print("os.path.dirname: ", os.path.dirname('C://python//my_file.txt'))
#-----------------------------------------------------------------------------os.path.exists()
'''
    描述：如果路径 path 存在，返回 True；如果路径 path 不存在，返回 False。
    语法：os.path.exists(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.exists:  ", os.path.exists(path))
#-----------------------------------------------------------------------------os.path.lexists()
'''
    描述：路径存在则返回True，路径损坏也返回True， 不存在，返回 False。
    语法：os.path.lexists
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.lexists:     ", (path))
#-----------------------------------------------------------------------------os.path.expanduser()
'''
    描述：把path中包含的"~"和"~user"转换成用户目录
    语法：os.path.expanduser(path)
'''
print("os.path.expanduser:  ", os.path.expanduser('~/wuzhengxiang/Desktop/股票数据分析/'))

#-----------------------------------------------------------------------------os.path.expandvars()
'''
    描述：根据环境变量的值替换path中包含的"$name"和"${name}"
    语法：os.path.expandvars(path)
'''
os.environ['KITTIPATH'] = 'D:/thunder'
path = '$KITTIPATH/train/2011_09_26_drive_0001_sync/proj_depth/velodyne_raw/image_02/0000000013.png'
print("os.path.expandvars:  ", os.path.expandvars(path))

#-----------------------------------------------------------------------------os.path.getatime()
'''
    描述：返回最近访问时间（浮点型秒数），从新纪元到访问时的秒数。
    语法：os.path.getatime(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.getatime:    ", os.path.getatime(path))
#-----------------------------------------------------------------------------os.path.getmtime()
'''
    描述：返回最近文件修改时间，从新纪元到访问时的秒数。
    语法：os.path.getmtime(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.getmtime:    ", os.path.getmtime(path))

#-----------------------------------------------------------------------------os.path.getctime()
'''
    描述：返回文件 path 创建时间，从新纪元到访问时的秒数。
    语法：os.path.getctime(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.getctime:    ", os.path.getctime(path))

#-----------------------------------------------------------------------------os.path.getsize()
'''
    描述：返回文件大小，如果文件不存在就返回错误
    语法：os.path.getsize(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\os_describe.py'
if os.path.exists(path):
    print("os.path.getsize: ", os.path.getsize(path))

#-----------------------------------------------------------------------------os.path.isabs()
print("os.path.isabs:   ", os.path.isabs(path))

#-----------------------------------------------------------------------------os.path.isfile()
'''
    描述：判断路径是否为文件, 是文件：True， 目录：False， 不存在：False， 
    语法：os.path.isfile(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\os_describe1.py'
print("os.path.isfile:  ", os.path.isfile(path))

#-----------------------------------------------------------------------------os.path.isdir()
'''
    描述：判断路径是否为目录
    语法：os.path.isdir(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb'
print("os.path.isdir:  ", os.path.isdir(path))

#-----------------------------------------------------------------------------os.path.join()
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb'
fileName = 'os_describe1.py'
print("os.path.join:    ", os.path.join(path, fileName))

#-----------------------------------------------------------------------------os.path.normcase()
'''
    描述：转换path的大小写和斜杠
    语法：os.path.normcase(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb'
print('os.path.normcase:    ', os.path.normcase(path))

#-----------------------------------------------------------------------------os.path.normpath()
'''
    描述：规范path字符串形式
    语法：os.path.normpath(path)
'''
print("os.path.normpath:    ", os.path.normpath('c://windows\\System32\\../Temp/'))

#-----------------------------------------------------------------------------os.path.realpath()
'''
    描述：返回path的真实路径
    语法：os.path.realpath(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb'
print("s.path.relpath:  ", os.path.relpath(path))

#-----------------------------------------------------------------------------os.path.samefile( )
'''
    描述：判断目录或文件是否相同
    语法：os.path.samefile(path1, path2)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
path1 = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\log'
print("os.path.samefile:    ", os.path.samefile(path, path1))

#-----------------------------------------------------------------------------os.path.split()
'''
    描述：把路径分割成 dirname 和 basename，返回一个元组
    语法：os.path.split(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\os_describe1.py'
print("os.path.split:   ", os.path.split(path))

#-----------------------------------------------------------------------------os.path.splitdrive()
'''
    描述：一般用在 windows 下，返回驱动器名和路径组成的元组
    语法：os.path.splitdrive(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\os_describe1.py'
print('os.path.splitdrive:  ', os.path.splitdrive(path))

#-----------------------------------------------------------------------------os.path.splitext()
'''
    描述：分割路径，返回路径名和文件扩展名的元组
    语法：os.path.splitext(path)
'''
path = r'D:\CompleteProgram\canKaoFiles\needsFiles\pythonDsb\os_describe1.py'
print("os.path.splitext:    ", os.path.splitext(path))

#-----------------------------------------------------------------------------os.path.walk()
'''
    描述：遍历path，进入每个目录都调用visit函数，visit函数必须有3个参数(arg, dirname, names)，
        dirname表示当前目录的目录名，names代表当前目录下的所有文件名，args则为walk的第三个参数
    语法：os.path.walk(path, visit, arg)
'''
abs_cur_dir = r'D:\CompleteProgram\canKaoFiles\needsFiles'
file_url=[]
for dirs,folders,files in os.walk(abs_cur_dir):
    for i in files:
            file_url.append(os.path.join(dirs,i))
print("os.path.walk:    ", file_url)
#-----------------------------------------------------------------------------

