"""fresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    # 给user里面加上一个路由
    path('account/',include("user.urls",namespace='user')),
    # 加入商品的路由
    path('goods/',include('goods.urls',namespace='goods')),
    path('cart/',include('cart.urls',namespace='cart')),
    path('order/',include('order.urls',namespace='order')),
    # 加入所搜的路由
    path('search/',include('haystack.urls')),
]
