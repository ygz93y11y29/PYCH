# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.days_attrs)
    .add_yaxis("商家A", Faker.days_values)
    .set_global_opts(
        #title_opts：标题配置     TitleOpts：标题配置项   title：主标题
        title_opts=opts.TitleOpts(title="Bar-DataZoom（slider-水平）"),
        #datazoom_opts:条形数据缩放滑块配置     DataZoomOpts:条形数据缩放滑块配置项
        datazoom_opts=opts.DataZoomOpts(),
    )
    .render("bar_datazoom_slider.html")
)
