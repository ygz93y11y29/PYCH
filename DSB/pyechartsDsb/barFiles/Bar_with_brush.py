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
        #title_opts：标题配置  TitleOpts标题配置项  title：主标题     subtitle：副标题
        title_opts=opts.TitleOpts(title="Bar-Brush示例", subtitle="我是副标题"),
        #BrushOpts：区域选择组件配置项
        brush_opts=opts.BrushOpts(),
    )
    .render("bar_with_brush.html")
)