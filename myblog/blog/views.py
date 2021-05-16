from django.shortcuts import render
import sys


# Create your views here.
# 首页
def index(request):
    return render(request, 'index.html', locals())


# 模板页
def base(request):
    return render(request, 'base.html', locals())


# 捕获500异常
def page_error(request):
    error = sys.exc_info()
    context = {
        'error': error
    }
    return render(request, '500.html', context=context)


# Python爬虫页面
def crawl(request, lid):
    print(lid)
    return render(request, 'crawl.html', locals())


# 文章详情页
def article_detail(request, sid):
    return render(request, 'detail.html', locals())


# 励志名言
def dream(request):
    return render(request, 'dream.html', locals())


# 数据分析页面
def data(request):
    return render(request, 'data.html', locals())
