"""mydemo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from django.conf.urls import url
import fa.views  #导入你应用下的views文件

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^db/', fa.views.db),
    url(r'^baidu/', fa.views.rebaidu),
    url(r'^index/', fa.views.index)     #逗号前是访问路径，后是views的函数名
]