# -*- coding:utf-8 -*-

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode
from pyecharts.faker import Faker

c = (
    Bar(
        init_opts=opts.InitOpts(
            # 图表背景颜色
            bg_color={"type": "pattern", "image": JsCode("img"), "repeat": "no-repeat"}
        )
    )
    .add_xaxis(Faker.choose())
    .add_yaxis("商家A", Faker.values())
    .add_yaxis("商家B", Faker.values())
    .set_global_opts(
        #标题配置项
        title_opts=opts.TitleOpts(
            #主标题
            title="Bar-背景图基本示例",
            #副标题
            subtitle="我是副标题",
            #主标题字体样式配置项  TextStyleOpts：文字样式配置项
            title_textstyle_opts=opts.TextStyleOpts(color="white"),
        )
    )
)
#添加js执行
c.add_js_funcs(
    """
    var img = new Image(); img.src = 'https://s2.ax1x.com/2019/07/08/ZsS0fK.jpg';
    """
)
c.render("bar_base_with_custom_background_image.html")



