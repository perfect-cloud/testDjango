from django.shortcuts import render
import datetime
import logging


# Create your views here.
def var(request):
    # 列表对象
    lists = ['Java', 'Python', 'C', 'C#', 'JavaScript']
    # 字典对象
    dicts = {'姓名': '张三', '年龄': 25, '性别': '男'}
    logger = logging.getLogger('django')
    logger.info("This is an error msg")
    return render(request, '3/var.html', {'lists': lists, 'dicts': dicts})


def for_label(request):
    dict1 = {'书名': 'Django开发', '价格': 80, '作者': '张三'}
    dict2 = {'书名': 'Python开发', '价格': 90, '作者': '李四'}
    dict3 = {'书名': 'Java开发', '价格': 100, '作者': '王五'}
    lists = [dict1, dict2, dict3]
    return render(request, '3/for_label.html', {'lists': lists})


def filter(request):
    str1 = "abcdefg"
    str2 = "ABCDEFG"
    slice_str = "1234567890"
    time_str = datetime.datetime.now()
    return render(request, '3/filter.html', {"str1": str1, "str2": str2, "slice_str": slice_str, "time_str": time_str})


def html_filter(request):
    html_addr = "<table border=1><tr><td>这是一个表格</td></td></table>"
    html_script = "<script language='javascript'>document.write('非法执行');</script> "
    return render(request, '3/html_filter.html', {"html_addr": html_addr, "html_script": html_script})


def diy_filter(request):
    dict1 = {'标题': '<table border=1><tr><td>这是一个表格</td></td></table>'}
    dict2 = {'标题': '<table border=2><tr><td>这是一个表格</td></td></table>'}
    dict3 = {'标题': '<table border=3><tr><td>这是一个表格</td></td></table>'}
    lists = [dict1, dict2, dict3]
    return render(request, '3/diy_filter.html', {"lists": lists})


def diy_tags(request):
    dict1 = {'标题': '<table border=1><tr><td>这是一个表格</td></td></table>'}
    dict2 = {'标题': '<table border=2><tr><td>这是一个表格</td></td></table>'}
    dict3 = {'标题': '<table border=3><tr><td>这是一个表格</td></td></table>'}
    lists = [dict1, dict2, dict3]
    return render(request, '3/diy_tags.html', {"lists": lists})


def show_info(request):
    return render(request, '3/show_info.html')


def welcome(request):
    return render(request, '3/welcome.html')


def welcome_include(request):
    return render(request, '3/base_include.html')