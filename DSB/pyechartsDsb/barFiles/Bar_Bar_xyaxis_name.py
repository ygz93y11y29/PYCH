# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        #标题配置项
        title_opts=opts.TitleOpts(title="Bar-XY 轴名称"),
        #Y轴配置项
        yaxis_opts=opts.AxisOpts(name="我是 Y 轴"),
        #X轴配置项
        xaxis_opts=opts.AxisOpts(name="我是 X 轴"),
    )
    .render("bar_xyaxis_name.html")
)
