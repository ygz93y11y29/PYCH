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
        title_opts=opts.TitleOpts(title="Bar-Y 轴 formatter"),
        #AxisOpts：坐标轴配置项    axislabel_opts:坐标轴标签配置项    LabelOpts：标签配置项   formatter：标签内容格式器
        yaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(formatter="{value} /月")),
    )
    .render("bar_yaxis_formatter.html")
)


