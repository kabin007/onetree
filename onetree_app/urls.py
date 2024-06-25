from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('menu/',views.menu,name="menu"),
    path('login/',views.loginpage,name="login"),
    path('signup/',views.signuppage,name="signup"),
    path('dashboard/',views.dashboard,name="dashboard"),
]