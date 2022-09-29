from django.urls import path
from . import views


urlpatterns = [
    path('', views.task_list, name='tasklist'),
    path('detail/<str:pk>/', views.taskdetail, name='detail'),
    path('edit/<str:pk>/', views.taskedit, name='edit'),
    path('delete/<str:pk>/', views.taskdelete, name='delete'),
    path('create/', views.taskcreate, name='create'),

    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.register_user, name='signup'),
]