from django.urls import path
from .views import logout_view, subscribe
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogo", views.catalogo, name="catalogo"),
    path("blog", views.blog, name="blog"),
    path("contacto", views.contacto, name="contacto"),
    path("login_registro", views.login_registro, name="login_registro"),
    path("nosotros", views.nosotros, name="nosotros"),
    path("registro", views.registro, name="registro"),
    path("perfil", views.perfil, name="perfil"),
    path("crud", views.crud, name="crud"),
    path("userAdd", views.userAdd, name="userAdd"),
    path("userDel/<str:pk>", views.userDel, name="userDel"),
    path("userEdit/<str:pk>", views.userEdit, name="userEdit"),
    path("userUpdate", views.userUpdate, name="userUpdate"),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('subscribe/', views.subscribe, name='suscripciones'),
    path('unsubscribe/', views.unsubscribe, name='unsubscribe'),

]
