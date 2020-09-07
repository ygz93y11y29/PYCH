# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), stack="stack1")
    .add_yaxis("商家B", Faker.values(), stack="stack1")
    .add_yaxis("商家C", Faker.values())
    #系列配置项      LabelOpts: 标签配置项
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #全局配置项     TitleOpts：标题配置项
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（部分）"))
    .render("bar_stack1.html")
)
