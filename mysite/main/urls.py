from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>', views.index, name = "index"),
    path('', views.v1, name = "view1"),
    path('v1/', views.v1, name = "view1"),
]
