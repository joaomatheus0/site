from django.urls import path
#from .views import IndexView
from .  import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Dashboard', views.dashboard, name='dashboard'),
    path('Register', views.register, name='register'),
    path('Logout', views.out, name="logout"),
    path('Settings',views.settings, name="settings"),
    path('Addinsta', views.add_insta, name="addinsta")
]
