# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    #TitleOpts:标题配置项        title： 主标题
    .set_global_opts(title_opts=opts.TitleOpts(title="Bar-MarkPoint（指定类型）"))
    .set_series_opts(
        #标签配置项
        label_opts=opts.LabelOpts(is_show=False),
        #标记点配置项
        markpoint_opts=opts.MarkPointOpts(
            #标记点数据
            data=[
                #标记点数据项
                opts.MarkPointItem(type_="max", name="最大值"),
                opts.MarkPointItem(type_="min", name="最小值"),
                opts.MarkPointItem(type_="average", name="平均值"),
            ]
        ),
    )
    .render("bar_markpoint_type.html")
)

