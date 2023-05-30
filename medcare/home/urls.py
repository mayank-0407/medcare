from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    
    path('', views.vhome,name="home"),  
    path('admin/', views.my_admin,name="admin"),  
    path('temp/', views.temp,name="temp"),  
    path('signin/', views.signin,name="signin"),  
    path('signup/', views.signup,name="signup"),  
    path('signout/', views.signout,name="signout"),  
    path('dashboard/', views.dashboard,name="dashboard"),  
    path('dashboard/add', views.addmedicine,name="add_med"),  
    path('dashboard/des', views.viewmed,name="view_med"),   
    
]