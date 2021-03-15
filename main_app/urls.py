from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('furniture/', views.furniture_index, name="index"),
    path('furniture/new/', views.furniture_new, name="new"),
    path('furniture/<int:furniture_id>/', views.furniture_detail, name='detail'),
    path('furniture/<int:furniture_id>/edit/', views.furniture_edit, name='edit'),
    path('furniture/<int:furniture_id>/delete/', views.furniture_delete, name='delete'),
    path('furniture/<int:furniture_id>/add_destroy/', views.add_destroy, name="add_destroy"),
    path('furniture/<int:furniture_id>/assoc_finish/<int:finish_id>/', views.assoc_finish, name="assoc_finish"),
    path('accounts/signup/', views.signup, name='signup'),
]
