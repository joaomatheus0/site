from django.urls import path
#from .views import IndexView
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('register', views.register, name='register'),
    path('logoutx', views.logoutx, name="logout")
]
