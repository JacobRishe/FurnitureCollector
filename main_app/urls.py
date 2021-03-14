from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('furniture/', views.furniture_index, name="index"),
    path('furniture/<int:furniture_id>/', views.furniture_detail, name='detail'),
    path('furniture/<int:furniture_id>/add_destroy/', views.add_destroy, name="add_destroy")
]


# path('accounts/signup', views.signup, name='signup'),
