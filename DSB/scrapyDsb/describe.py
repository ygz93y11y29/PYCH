# -*- coding: utf-8 -*-
'''
    分布式：  scrapyd安装， scrapyd， scrapyd用自定义redis去重， scrapyd用scrapy_redis去重， gerapy安装,
'''

#------------------------------------------------------------------------------------scrapyd安装
'''
scrapyd安装:
    -->pip install scrapyd
    Windows:
        -->pip install scrapyd-client
    scrapyd-client连接scrapyd服务
        -->vim /usr/lib/python2.7/site-packages/scrapyd/default_scrapyd.conf     
            default_scrapyd.conf>修改bind_address = 0.0.0.0
    重启scrapyd服务
        -->scrapyd
    验证：
        浏览器：http://IP:6800/
        如果不成功：
            -->systemctl stop firewalld.service
            -->firewall-cmd --zone=public --add-port=6800/tcp --permanent
    linux后台启动脚本:
        -->setsid scrapyd   #后台开启服务
        -->ps -ef | grep -i scrapyd 
        -->kill -9 PID
    linux脚本：
        在/etc/init.d 目录下面，新建文件scrapyd脚本：
            #!/bin/bash
            PORT=6800
            HOME="/var/scrapyd" #crapyd运行的目录，如果没有需要新建
            BIN="/usr/local/bin/scrapyd"    #BIN为scrapyd安装目录。以个人实际情况修改
             
            pid=`netstat -lnopt | grep :$PORT | awk '/python/{gsub(/\/python/,"",$7);print $7;}'`
            start() {
               if [ -n "$pid" ]; then
                  echo "server already start,pid:$pid"
                  return 0
               fi
             
               cd $HOME
               nohup $BIN >> $HOME/scrapyd.log 2>&1 &
               echo "start at port:$PORT"
            }
             
            stop() {
               if [ -z "$pid" ]; then
                  echo "not find program on port:$PORT"
                  return 0
               fi
             
               #结束程序，使用讯号2，如果不行可以尝试讯号9强制结束
               kill -9 $pid
               echo "kill program use signal 9,pid:$pid"
            }
             
            status() {
               if [ -z "$pid" ]; then
                  echo "not find program on port:$PORT"
               else
                  echo "program is running,pid:$pid"
               fi
            }
             
            case $1 in
               start)
                  start
               ;;
               stop)
                  stop
               ;;
               status)
                  status
               ;;
               *)
                  echo "Usage: {start|stop|status}"
               ;;
            esac
             
            exit 0
            
        赋予可执行权限：
            -->chmod u+x scrapyd
            -->ll
        测试:
            开启服务:
                -->service scrapyd start
            查看状态:
                -->service scrapyd status
            关闭服务:
                -->service scrapyd stop
'''

#------------------------------------------------------------------------------------scrapyd
'''
第一步：启动客户端/服务端的scrapyd:
    -->scrapyd
'''
'''
第二步：修改.cfg文件， 执行部署命令：
    scrapy.cfg>[deploy]
                url = http://192.168.10.3:6800/
                project = fsScrapySpider
    -->scrapyd-deploy
'''
'''
第三步：
    查看远端服务器上面的爬虫
    -->curl http://192.168.10.3:6800/listprojects.json
    移除远程服务器上面部署的爬虫工程
    -->curl http://192.168.10.3:6800/delproject.json -d project=fsScrapySpider
    启动爬虫
    -->curl http://192.168.10.3:6800/schedule.json  -d project=fsScrapySpider -d spider=jjkxSpider
    取消爬虫
    -->curl http://192.168.10.3:6800/cancel.json -d project=fsScrapySpider -d job=c5af7a94afa011eab916c03fd5fc3c99
'''

#------------------------------------------------------------------------------------scrapyd用自定义redis去重
'''
第一步：添加文件dupeFilter.py:重写request_seen
        class DupFilter(BaseDupeFilter):
            def __init__(self):
                self.conn = redis.Redis(host='192.168.10.3', port=6379, db=15, password='123456')
            def request_seen(self, request):
                """
                检测当前请求是否已经被访问过
                :param request: 
                :return: True表示已经访问过；False表示未访问过
                """
                fid = request_fingerprint(request)
                result = self.conn.sadd('visited_urls', fid)
                if result == 1:
                    return False
                return True
'''
'''
第二步：添加过滤：
    settings.py>DUPEFILTER_CLASS = 'fsScrapySpider.dupeFilter.DupFilter'
'''

#------------------------------------------------------------------------------------scrapyd用scrapy_redis去重
'''
第一步：继承RedisSpider，并去除spider的start_urls，添加redis_key = 'jjkxSpider:start_urls'
    class JjkxspiderSpider(RedisSpider):
        ...
        # start_urls = ['http://edu.foshan.gov.cn/kx/jjkx/index.html']
        redis_key = 'jjkxSpider:start_urls'
        ...
'''
'''
第二步：settings添加配置：
    去重规则对应处理的类
        settings.py>    DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
    指定使用scrapy-redis的调度器
        settings.py>    SCHEDULER = "scrapy_redis.scheduler.Scheduler" 
    在redis中保持scrapy-redis用到的各个队列，从而允许暂停和暂停后恢复，也就是不清理redis queues 
        settings.py>    SCHEDULER_PERSIST = True
    redis链接：
        settings.py>    REDIS_URL = "redis://root:123456@192.168.10.3:6379/15"
'''
'''
第三步：新建add_startUrl.py 负责发送start_urls
'''
'''
第四步：添加去重规则，（可选）
    添加去重文件
    修改settings中的DUPEFILTER_CLASS
    settings.py>    DUPEFILTER_CLASS = "fsScrapySpider.dupeFilter.RedisDupeFilter"
'''

#------------------------------------------------------------------------------------Gerapy
'''
第一步：安装gerapy:
    -->pip install gerapy
    -->gerapy
'''
'''
第二步：初始化gerapy
    -->gerapy init
    执行后会在当前目录下生成一个名字为gerapy的文件夹
    -->cd gerapy
    接着进入该文件夹下，可以看到project文件家说明初始化成功
'''
'''
第三步：初始化数据库
    -->gerapy migrate
    （此命令在gerapy目录下执行）
    会在gerapy目录下生成一个sqlite数据库，同时创建数据表
'''
'''
第四步：.运行gerapy服务
    -->gerapy runserver
    （如果电脑在打开酷狗音乐，请关闭再访问：因为端口是一样的
'''
'''
第五步：访问gerapy管理界面
    浏览器>http://localhost:8000/
'''
'''
第六步：如果遇到：需要登录账号密码 ，但是我们没有设置的话，可以执行：
        -->gerapy migrate 
        初始化数据库
        gerapy createsuperuser
        创建超级用户
            （之后就是输入Username:，
                        Email:--可以不用写直接回车，
                        Password:）
'''
'''
第七步：运行gerapy
    -->gerapy runserver
'''
#------------------------------------------------------------------------------------Scrapy命令行功能
'''
第一部分：	全局命令	

	1.startproject
		> scrapy startproject [project_name]
		> 创建名为mySpider的Scrapy项目
		$ scrapy startproject mySpider

	2.settings
		> scrapy settings [options]
		> 当项目运行时，输出项目的设定值，否则输出Scrapy的默认设定值
		$ scrapy settings --get BOT_NAME scrapybot
		$ scrapy settings --get DOWNLOAD_DELAY 0

	3.runspider
		> scrapy runspider <spider_file.py>
		> 未创建项目的情况下，运行一个编写好的spider模块
		$ scrapy runspider testSpider.py

	4.shell
		> scrapy shell [url]
		> 启动Scrapy shell，url可选
		$ scrapy shell "http://www.baidu.com"
		$ scrapy shell file:///D:/CompleteProgram/dazhongDianPingFiles/daZhongDianPingSpider/list.html
		$ scrapy shell D:/CompleteProgram/dazhongDianPingFiles/daZhongDianPingSpider/list.html
		$ scrapy shell -s USER_AGENT='Mozilla/5.0...'

	5.fetch
		> scrapy fetch <url>
		> 使用Scrapy下载器(downloader)下载给定的url，并将获取的内容输出
		> 命令以spider下载页面的方式获取页面，如果在项目中运行，fetch将会使用项目中spider的属性访问；如果在非项目中运行，则会使用默认Scrapy downloader的设定
		$ scrapy fetch --nolog "http://www.baidu.com"
		$ scrapy fetch --nolog --headers "http://www.baidu.com"

	6.view
		> scrapy view <url>
		> 在浏览器中打开url，并以Scrapy spider获取到的形式显示
		> 与view(response)效果一样
		$ scrapy view "http://www.baidu.com"

	7.version
		> scrapy version [-v]
		> 输出Scrapy版本
		> 配合-v运行时，同时输出Python、Twisted以及平台信息，方便bug提交

	8.bench
		> scrapy bench
		> 用于运行benchmark测试，测试Scrapy在硬件上的效率
'''

'''
第二部分：	项目命令，必须在Scrapy项目中运行

	1.crawl
		> scrapy crawl <spider>
		> 使用spider进行爬取
		$ scrapy crawl mySpider

	2.check
		> scrapy check [-l] <spider>
		> 运行contract检查
		$ scrapy check -l

	3.list
		> scrapy list
		> 列出当前项目中所有的可用的spider，每行输出一个

	4.edit
		> scrapy edit <spider>
		> 使用设定的编辑器编辑给定的spider，此命令仅提供一个快捷方式，可自由选择编辑器
		$ scrapy edit mySpider

	5.parse
		> scrapy parse <url> [options]
		> 获取给定的url并使用相应的spider分析处理
		> 如果提供--callback选项，则使用spider中的解析方法进行处理。
		> 支持的选项：
		>>> --spider=SPIDER:跳过自动检测spider并强制使用特定的spider
		>>> --a NAME=VALUE:设定spider参数（可能被重复）
		>>> --callback or -c:spider中用于解析response的回调函数
		>>> --pipelines:在pipelin中处理item
		>>> --rules or r:使用CrawlSpider规则来发现用于解析response的回调函数
		>>> --noitems:不显示爬取到的item
		>>> --nolinks:不显示提取到的链接
		>>> --nocolour:避免使用pygments对输出着色
		>>> --depth or -d:指定跟进链接请求的层次数（默认：1）
		>>> --verbose or -v:显示每个请求的详细信息
		$ scrapy parse "http://www.baidu.com"

	6.genspider
		> scrapy genspider [-t template] <name> <domain>
		> 在当前项目中创建spider
		> 这是创建spider的快捷方式，可使用提前定义好的模板来生成spider，也可自己创建spider的源文件
		$ scrapy genspider -l
		> 显示有哪些模板
		$ scrapy genspider -d basic
		$ scrapy genspider -t basic example example.com

	7.deploy
		> scrapy deploy [<target:project> | -l <target> | -L]
		> 部署项目到Scrapyd服务
'''

#------------------------------------------------------------------------------------





















