from django.urls import path

from . import views

urlpatterns = [

    path('registerUser', views.registerUser, name='registerUser'),
    path('login', views.login, name='login'),
    # path('createBill', views.login, name='createBill'),
    # path('showAllBill', views.login, name='showAllBill'),
    # path('UpdateBill', views.login, name='UpdateBill'),
    # path('CreateDailySheet', views.CreateDailySheet, name='CreateDailySheet'),
    # path('CreateKhatiyan', views.CreateKhatiyan, name='CreateKhatiyan'),
    # path('UpdateKhatiyan', views.UpdateKhatiyan, name='UpdateKhatiyan'),
    # path('DeleteKhatiyan', views.DeleteKhatiyan, name='DeleteKhatiyan'),
    # path('ShowStaffProfile', views.ShowStaffProfile, name='ShowStaffProfile'),
    # path('CreateStaffProfile', views.CreateStaffProfile, name='CreateStaffProfile'),
    # path('UpdateUserProfile', views.UpdateUserProfile, name='UpdateUserProfile'),
    # path('ShowPartyProfile', views.ShowPartyProfile, name='ShowPartyProfile'),
    # path('CreatePartyProfile', views.CreatePartyProfile, name='CreatePartyProfile'),
    # path('UpdatePartyProfile', views.UpdatePartyProfile, name='UpdatePartyProfile'),
    path('createProduct', views.createProduct, name='createProduct'),







]
