"""furniture1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from users1 import views as v
from admins1 import views as v1
from django.conf import settings
from django.conf.urls.static import static

app_name='users1'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',v.index,name="index"),
    path('reg/',v.reg,name="reg"),
    path('log/',v.log,name="login"),
    path('home/',v.home,name="home"),
    path('profile/',v.profile,name="profile"),
    path('alogin/',v1.alogin,name="alogin"),
    path('addproduct/',v1.addproduct,name='addproduct'),
    path('viewproduct/',v1.viewproduct,name='viewproduct'),
    path('ahome/',v1.ahome,name='ahome'),
    path('profile1/',v1.profile1,name='profile1'),
    path('products/',v.products,name="products"),
    path('products/<int:id>/',v.products,name='products'),
    path('buyproduct/',v.buyproduct,name='buyproduct'),
    path('buyproduct/<int:id>/buy/',v.buyproduct,name='buyproduct'),
    path('purchase/',v.purchase,name='purchase'),
    path('lastview/',v.lastview,name='lastview'),
    path('logout/',v.logout,name='logout'),
    path('alogout',v1.alogout,name='alogout'),
    path('alastview',v1.alastview,name='alastview')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
