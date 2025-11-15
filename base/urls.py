from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('room/<str:pk>/',views.room,name="room"),
    path('update_room/<int:pk>/',views.updateRoom,name="update_room"),
    path('delete_room/<int:pk>/',views.deleteRoom,name="delete_room"),
    path('register',views.registerView,name="register"),
    path('login',views.loginView,name="login"),
    path('logout',views.logoutView,name="logout"),
    path('profile/<int:pk>',views.UserProfile,name="profile"),
]