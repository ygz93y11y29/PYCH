# -*- coding:utf-8 -*-
'''
    直方图/条形图添加工具配置项，去掉图例显示
'''
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.faker import Faker

c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        #title_opts;标题配置   TitleOpts:标题配置项   title：主标题
        title_opts=opts.TitleOpts(title="Bar-显示 ToolBox"),
        #toolbox_opts:工具箱配置     ToolboxOpts:工具箱配置项
        toolbox_opts=opts.ToolboxOpts(),
        #legend_opts:图例配置   LegendOpts:图例配置项   is_show: 是否显示
        legend_opts=opts.LegendOpts(is_show=False),
    )
    .render("bar_toolbox.html")
)