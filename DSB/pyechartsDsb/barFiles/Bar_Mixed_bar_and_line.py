# -*- coding:utf-8 -*-

import pyecharts.options as opts
from pyecharts.charts import Bar, Line

"""
Gallery 使用 pyecharts 1.1.0
参考地址: https://www.echartsjs.com/examples/editor.html?c=mix-line-bar

目前无法实现的功能:

1、暂无
"""

x_data = ["1月", "2月", "3月", "4月", "5月", "6月", "7月", "8月", "9月", "10月", "11月", "12月"]

bar = (
    Bar(init_opts=opts.InitOpts(width="1600px", height="800px"))
    # xaxis_data：刻度数据
    .add_xaxis(xaxis_data=x_data)
    #series_name：系列名称   yaxis_data：系列数据     label_opts：标签配置     LabelOpts：标签配置项   is_show：是否显示标签
    .add_yaxis(
        series_name="蒸发量",
        yaxis_data=[
            2.0,
            4.9,
            7.0,
            23.2,
            25.6,
            76.7,
            135.6,
            162.2,
            32.6,
            20.0,
            6.4,
            3.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    .add_yaxis(
        series_name="降水量",
        yaxis_data=[
            2.6,
            5.9,
            9.0,
            26.4,
            28.7,
            70.7,
            175.6,
            182.2,
            48.7,
            18.8,
            6.0,
            2.3,
        ],
        label_opts=opts.LabelOpts(is_show=False),
    )
    #extend_axis：扩展 X/Y 轴    yaxis：新增 Y 坐标轴配置项   AxisOpts：坐标轴配置项  name：坐标轴名称 type_：坐标轴类型    min_：指定 visualMapPiecewise 组件的最小值
               #max_：指定 visualMapPiecewise 组件的最大值   interval：强制设置坐标轴分割间隔。   axislabel_opts：坐标轴标签配置项
    .extend_axis(
        yaxis=opts.AxisOpts(
            name="温度",
            type_="value",
            min_=0,
            max_=25,
            interval=5,
            axislabel_opts=opts.LabelOpts(formatter="{value} °C"),
        )
    )
    .set_global_opts(
        #tooltip_opts：提示框配置   TooltipOpts：提示框配置项 is_show：是否显示提示框组件   trigger：触发类型  axis_pointer_type：指示器类型
        tooltip_opts=opts.TooltipOpts(
            is_show=True, trigger="axis", axis_pointer_type="cross"
        ),
        #X轴 配置    AxisOpts：坐标轴配置项   type_：坐标轴类型     axispointer_opts：坐标轴指示器配置项  AxisPointerOpts：坐标轴指示器配置项
        xaxis_opts=opts.AxisOpts(
            type_="category",
            axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
        ),
        #Y轴 配置    AxisOpts：坐标轴配置项  name：坐标轴名称 type_：坐标轴类型 min_：指定 visualMapPiecewise 组件的最小值
               #max_：指定 visualMapPiecewise 组件的最大值   interval：强制设置坐标轴分割间隔。
        yaxis_opts=opts.AxisOpts(
            name="水量",
            type_="value",
            min_=0,
            max_=300,
            interval=50,
            #axislabel_opts：坐标轴标签配置项
            axislabel_opts=opts.LabelOpts(formatter="{value} ml"),
            #AxisTickOpts:坐标轴指示器配置项
            axistick_opts=opts.AxisTickOpts(is_show=True),
            #SplitLineOpts:分割线配置项
            splitline_opts=opts.SplitLineOpts(is_show=True),
        ),
    )
)


#折线图
line = (
    Line()
    #新增 X 轴数据   xaxis_data：数据
    .add_xaxis(xaxis_data=x_data)
    #新增 Y 轴数据
    .add_yaxis(
        #series_name：系列名称
        series_name="平均温度",
        #使用的 y 轴的 index，在单个图表实例中存在多个 y 轴的时候有用。
        yaxis_index=1,
        #系列数据
        y_axis=[2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2],
        #标签配置项
        label_opts=opts.LabelOpts(is_show=False),
    )
)

#overlap：层叠多图
bar.overlap(line).render("mixed_bar_and_line.html")
