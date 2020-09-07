# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values(), stack="stack1")
    .add_yaxis("商家B", Faker.values(), stack="stack1")
    #set_series_opts：系统配置项        label_opts：标签配置      LabelOpts：标签配置项  is_show：是否显示标签。
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
    #set_global_opts:全局配置项     title_opts->标题设置   TitleOpts->标题配置项  title->主标题文本
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-堆叠数据（全部）"))
    .render("bar_stack0.html")
)
