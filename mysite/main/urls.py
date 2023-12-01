from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name = "index"),
    path('home', views.home, name = "home"),
    path('create/', views.create, name = "create"),
    path('view/', views.view, name = "view"),
    path('view2/', views.view2, name = "view2"),
    path('', views.home, name = "start")
]
