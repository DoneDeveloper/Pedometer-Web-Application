from django.urls import path
from . import views


urlpatterns = [
    path('', views.loginPage, name="login"),
    path('dashboard/', views.home, name="home"),
    path('logout/', views.logoutUser, name="logout"),
    path('register/', views.registerPage, name="register"),

    path('submit_a_day/<str:pk>/', views.addSteps, name="add_steps"),
]
