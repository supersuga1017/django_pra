"""
URL configuration for private_diary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD
from django.urls import path,include
from django.contrib.staticfiles.urls import static

=======
from django.urls import path
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052


from django.urls import path,include

from django.contrib import admin
from django.urls import path,include

<<<<<<< HEAD
from . import settings_common,settings_dev

=======
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),

<<<<<<< HEAD
    path('accounts/', include('allauth.urls')),
]

# 開発サーバーでメディアを配信できるように設定
urlpatterns += static(settings_common.MEDIA_URL,document_root = settings_dev.MEDIA_ROOT)
=======
    # path('accounts/', include('allauth.urls')),
]
>>>>>>> ce8f1603a7b4955e9d1ec2996b6376a5e5e36052
