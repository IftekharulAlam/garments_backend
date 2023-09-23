from django.urls import path
from .views import *


urlpatterns = [

    path('registerUser', loginRegister.registerUser, name='registerUser'),
    path('login', loginRegister.login, name='login'),

    path('createKhatiyan', khatiyan.createKhatiyan, name='createKhatiyan'),

    path('getKhatiyanList', khatiyan.getKhatiyanList, name='getKhatiyanList'),
    path('getKhatiyanDetails', khatiyan.getKhatiyanDetails, name='getKhatiyanDetails'),


    path('getStaffKhatiyanList', staffKhatiyan.getStaffKhatiyanList,
         name='getStaffKhatiyanList'),
    path('getKhatiyanDetailsStaff', staffKhatiyan.getKhatiyanDetailsStaff,
         name='getKhatiyanDetailsStaff'),
    path('getProfileDetailsStaff', staffProfile.getProfileDetailsStaff,
         name='getProfileDetailsStaff'),

    path('createProduct', products.createProduct, name='createProduct'),
    path('addProduct', products.addProduct, name='addProduct'),
    path('getProductsList', products.getProductsList, name='getProductsList'),
    path('getProductsSizeList', products.getProductsSizeList,
         name='getProductsSizeList'),
    path('getProductProductionDetails', products.getProductProductionDetails,
         name='getProductProductionDetails'),
    path('getProductsSizeList', products.getProductsSizeList,
         name='getProductsSizeList'),
    path('createParty', partyKhatiyan.createParty, name='createParty'),
    path('getPartyList', partyProfile.getPartyList, name='getPartyList'),
    path('getPartyKhatiyanDetails', partyKhatiyan.getPartyKhatiyanDetails,
         name='getPartyKhatiyanDetails'),
    path('getProductDetails', products.getProductDetails,
         name='getProductDetails'),

    path('createDailysheetJoma', dailySheet.createDailysheetJoma,
         name='createDailysheetJoma'),
    path('createDailysheetKhoroch', dailySheet.createDailysheetKhoroch,
         name='createDailysheetKhoroch'),
    path('dailysheetJomaKhorochList', dailySheet.dailysheetJomaKhorochList,
         name='dailysheetJomaKhorochList'),

    path('createBill', bill.createBill,
         name='createBill'),


]
