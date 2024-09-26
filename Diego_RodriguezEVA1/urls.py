"""
URL configuration for Diego_RodriguezEVA1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from Diego_RodriguezEVA1_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('usuario/', views.renderTemplate),
    path('electronicos/', views.electronicos),
    path('electronicos/electronico1/', views.electronico1),
    path('electronicos/electronico2/',views.electronico2),
    path('electronicos/electronico3/', views.electronico3),
    path('perifericos/',views.perifericos),
    path('perifericos/periferico1/',views.periferico1),
    path('perifericos/periferico2/', views.periferico2),
    path('perifericos/periferico3/',views.periferico3),
    path('accesorios/', views.accesorios),
    path('accesorios/accesorio1/',views.accesorio1),
    path('accesorios/accesorio2/',views.accesorio2),
    path('accesorios/accesorio3/',views.accesorio3),

]
