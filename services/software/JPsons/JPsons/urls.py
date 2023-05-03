"""
URL configuration for JPsons project.

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
from django.urls import path,include
from customer import views
from product import views as v1
from image import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('jp/',views.home),
    path('cshow/',views.cshow),
    path('cform/',views.cform),
    path('accounts/',include('django.contrib.auth.urls')),
    path('logout/',views.logout),
    path('signup/',views.signup),
    path('insert/',views.insert),
    path('update/',views.update),
    path('delete/',views.delete),
    path('signup/',views.signup),
    path('pshow/',v1.pshow),
    path('pform/',v1.pform),
    path('api/service/details/',v1.papiview.as_view()),
    path('api/service/update/<int:pk>',v1.papidel.as_view()),
    path('display/',v2.pimgshow),
    path('upload/',v2.pimgform),
    path('video/',v2.videoshow),
    path('vupload/',v2.videoupload),
]
