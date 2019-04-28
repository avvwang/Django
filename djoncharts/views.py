#coding=utf8

from django.shortcuts import render

# Create your views here.
# myechartsite/djoncharts/views.py

# from __future__ import unicode_literals
from django.shortcuts import render
import math
from django.http import HttpResponse
from django.template import loader
from pyecharts import Line3D


# from pyecharts.constants import DEFAULT_HOST
DEFAULT_HOST=""



def pyechart3d(request):
    # template = loader.get_template('djoncharts/pyecharts.html')
    l3d = bar_test()
    context = dict(
        myechart=l3d.render_embed(),
        host=DEFAULT_HOST,
        script_list=l3d.get_js_dependencies()
    )
    return render(request,"djoncharts/pyecharts.html",context=context)
    # return HttpResponse(template.render(context, request))


def line3d():
    _data = []
    for t in range(0, 25000):
        _t = t / 1000
        x = (1 + 0.25 * math.cos(75 * _t)) * math.cos(_t)
        y = (1 + 0.25 * math.cos(75 * _t)) * math.sin(_t)
        z = _t + 2.0 * math.sin(75 * _t)
        _data.append([x, y, z])
    range_color = [
        '#313695', '#4575b4', '#74add1', '#abd9e9', '#e0f3f8', '#ffffbf',
        '#fee090', '#fdae61', '#f46d43', '#d73027', '#a50026']
    line3d = Line3D("3D line plot demo", width=1200, height=600)
    line3d.add("", _data, is_visualmap=True,
               visual_range_color=range_color, visual_range=[0, 30],
               is_grid3D_rotate=True, grid3D_rotate_speed=180)
    print(line3d)
    return line3d


def bar_test():
    from pyecharts import Bar
    bar = Bar("我的第一个图表", "这里是副标题")
    bar.use_theme('dark')  # 暗色背景色
    bar.add("服装",2
            ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"],  # 横坐标
            [5, 20, 36, 10, 75, 90],is_more_utils=True)  # 纵坐标
    return bar

def Line():
    from pyecharts import Line, EffectScatter, Overlap
    attr = ['衬衫', '羊毛衫', '雪纺衫', '裤子', '高跟鞋', '袜子']
    v1 = [5, 20, 36, 10, 10, 90]
    line = Line('线性_闪烁图示例')
    line.add('', attr, v1, is_random=True,is_more_utils=True  )
    es = EffectScatter()
    es.add('', attr, v1, effect_scale=8)  # 闪烁
    overlop = Overlap()
    overlop.add(line)  # 必须先添加line,在添加es
    overlop.add(es)
    return overlop
