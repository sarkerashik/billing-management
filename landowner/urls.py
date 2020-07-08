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
    path('bill-categories',views.bill_categories,name='bill_categories'),
    path('bill-categories/create',views.createBill_Categories,name='createbill_categories'),
    path('bill-categories/edit/<nid>',views.editBill_categories,name='editbill_categories'),
    path('bill-categories/delete/<nid>',views.deleteBill_categories,name='deletebill_categories'),
    path('bills',views.bills,name='bills'),
    path('bills/create',views.createBills,name='createbills'),
    path('bills/edit/<nid>',views.editBills,name='editbills'),
    path('bills/delete/<nid>',views.deleteBills,name='deletebills'),
]  

     