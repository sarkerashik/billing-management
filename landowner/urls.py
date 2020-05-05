from django.urls import path
from .import views


urlpatterns=[
    path('',views.mainhome,name='mainhome'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('landowner/create',views.createLandowner,name='createlandowner'),
    path('landowner',views.landowner,name='landowner'),
    path('landowner/edit/<nid>',views.editLandowner,name='editlandowner'),
    path('landowner/delete/<nid>',views.deleteLandowner,name='deletelandowner'),
] 