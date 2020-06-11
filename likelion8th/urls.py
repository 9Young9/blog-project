"""likelion8th URL Configuration

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
from django.urls import path,include
import blog.views   # blog 앱에 있는 views 파일을 가져온다.
# 아래는 미디어 할 때 쓰는 것들
import blog.urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',blog.views.list, name = "list"),
    path('blog/<int:blog_id>', blog.views.detail, name = "detail"), # int -> 객체 번호가 따로 주어진다
    path('blog/new', blog.views.new, name = "new"),
    path('blog/create',blog.views.create, name = "create"),
    path('blog/edit/<int:blog_id>', blog.views.edit, name = "edit"),
    path('blog/update/<int:blog_id>', blog.views.update, name = "update"),
    path('blog/delete/<int:blog_id>', blog.views.delete, name = "delete"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 위에 붙여서 쓰는 거 말고 이렇게 해도 됨!

# python manage.py createsuperuser -> admin 페이지 계정 생성