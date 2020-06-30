"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index/'),  # 首页
    path('base/', views.base, name='base/'),  # 母版
    path('crawl-<int:lid>.html', views.crawl, name='crawl/'),  # Python爬虫
    path('article_detail-<int:sid>.html',views.article_detail,name='article_detail/'),  # 文章详情页
    path('dream/',views.dream,name='dream/'),  # 励志名言
    path('data/',views.data,name='data/'),  # 数据分析页面
]
