from django.urls import path
from . import views

urlpatterns = [
    path("index", views.index, name="index"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("blog", views.blog, name="blog"),
    path("contacto", views.contacto, name="contacto"),
    path("login_registro", views.login_registro, name="login_registro"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("registro", views.registro, name="registro"),
    path("suscripciones", views.suscripciones, name="suscripciones"),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/ <str:pk>", views.userDel, name="userDel"),
    path("userEdit/ <str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path('login/', views.login, name='login'),
]
