# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    #color:系列 label 颜色
    .add_yaxis("商家A", Faker.days_values, color=Faker.rand_color())
    .set_global_opts(
        #标题配置项      title：主标题
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-垂直）"),
        #区域缩放配置项    orient：布局方式是横还是竖。
        datazoom_opts=opts.DataZoomOpts(orient="vertical"),
    )
    .render("bar_datazoom_slider_vertical.html")
)



