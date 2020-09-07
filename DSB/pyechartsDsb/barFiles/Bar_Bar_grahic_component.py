# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker


c = (
    Bar()
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Bar-Graphic 组件示例"),
        #组件配置
        graphic_opts=[
            #原生组件配置
            opts.GraphicGroup(
                # 图形的配置项
                    #原生图形配置项
                graphic_item=opts.GraphicItem(
                    #旋转（rotation）：默认值是 0。表示旋转的弧度值。正值表示逆时针旋转
                    rotation=JsCode("Math.PI / 4"),
                    # 决定此图形元素在定位时，对自身的包围盒计算方式
                    bounding="raw",
                    #描述怎么根据父元素进行定位。
                    right=110,
                    bottom=110,
                    z=100,
                ),
                children=[
                    #原生图形矩形配置项
                    opts.GraphicRect(
                        #graphic_item：图形的配置项
                            #GraphicItem：原生图形配置项
                        graphic_item=opts.GraphicItem(
                            #left：描述怎么根据父元素进行定位。    top ：配置和 left 及 right 相同    z 方向的高度，决定层叠关系。
                            left="center", top="center", z=100
                        ),
                        # 图形的形状配置项，
                            #原生图形形状配置项   width： 图形元素的宽度。    height： 图形元素的高度。
                        graphic_shape_opts=opts.GraphicShapeOpts(width=400, height=50),
                        # 图形基本配置项
                            #原生图形基础配置项
                        graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                            # 填充色
                            fill="rgba(0,0,0,0.3)"
                        ),
                    ),
                    #原生图形文本配置项
                    opts.GraphicText(
                        #GraphicItem：原生图形配置项
                            #left：描述怎么根据父元素进行定位。   top ：配置和 left 及 right 相同    z 方向的高度，决定层叠关系。
                        graphic_item=opts.GraphicItem(
                            left="center", top="center", z=100
                        ),
                        #图形文本样式的配置项
                            #原生图形文本样式配置项
                        graphic_textstyle_opts=opts.GraphicTextStyleOpts(
                            #text：文本块文字。可以使用 \n 来换行
                            text="pyecharts bar chart",
                            # font：字体大小、字体类型、粗细、字体样式。
                            font="bold 26px Microsoft YaHei",
                            # 图形基本配置项
                                # 原生图形基础配置项
                            graphic_basicstyle_opts=opts.GraphicBasicStyleOpts(
                                # 填充色
                                fill="#fff"
                            ),
                        ),
                    ),
                ],
            )
        ],
    )
    .render("bar_graphic_component.html")
)
