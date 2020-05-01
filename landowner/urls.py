from django.urls import path
from .import views


urlpatterns=[
    path('',views.mainhome,name='mainhome'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('createland<nid>',views.createland,name='createland'),
    path('showland<usid>',views.showland,name='showland'),
    path('edit<nid><usid>',views.edit,name='edit'),
    path('delete<nid><usid>',views.delete,name='delete'),
]