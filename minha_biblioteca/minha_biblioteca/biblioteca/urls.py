from django.urls import path
from . import views

urlpatterns = [
    path('registro/', views.registro, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('adicionar_livro/', views.adicionar_livro, name='adicionar_livro'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('personalizar/', views.personalizar, name='personalizar'),
]
