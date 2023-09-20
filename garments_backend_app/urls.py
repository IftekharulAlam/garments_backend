from django.urls import path

from . import views

urlpatterns = [

    path('registerUser', views.registerUser, name='registerUser'),
    path('login', views.login, name='login'),

    path('createKhatiyan', views.createKhatiyan, name='createKhatiyan'),

    path('getKhatiyanList', views.getKhatiyanList, name='getKhatiyanList'),
    path('getKhatiyanDetails', views.getKhatiyanDetails, name='getKhatiyanDetails'),


    path('getStaffKhatiyanList', views.getStaffKhatiyanList,
         name='getStaffKhatiyanList'),
    path('getKhatiyanDetailsStaff', views.getKhatiyanDetailsStaff,
         name='getKhatiyanDetailsStaff'),
    path('getProfileDetailsStaff', views.getProfileDetailsStaff,
         name='getProfileDetailsStaff'),

    path('createProduct', views.createProduct, name='createProduct'),
    path('addProduct', views.addProduct, name='addProduct'),
    path('getProductsList', views.getProductsList, name='getProductsList'),
    path('getProductsSizeList', views.getProductsSizeList,
         name='getProductsSizeList'),
    path('createParty', views.createParty, name='createParty'),
    path('getPartyList', views.getPartyList, name='getPartyList'),
    path('getPartyKhatiyanDetails', views.getPartyKhatiyanDetails,
         name='getPartyKhatiyanDetails'),

    path('createDailysheetJoma', views.createDailysheetJoma,
         name='createDailysheetJoma'),
    path('createDailysheetKhoroch', views.createDailysheetKhoroch,
         name='createDailysheetKhoroch'),
    path('dailysheetJomaKhorochList', views.dailysheetJomaKhorochList,
         name='dailysheetJomaKhorochList'),

]
