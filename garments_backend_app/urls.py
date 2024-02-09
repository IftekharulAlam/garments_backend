from django.urls import path
from .views import *
from django.conf.urls.static import static
urlpatterns = [

    path('registerUser', loginRegister.registerUser, name='registerUser'),
    path('login', loginRegister.login, name='login'),

    path('createKhatiyan', khatiyan.createKhatiyan, name='createKhatiyan'),

    path('getKhatiyanList', khatiyan.getKhatiyanList, name='getKhatiyanList'),
    path('getKhatiyanListAll', khatiyan.getKhatiyanListAll, name='getKhatiyanListAll'),
    path('getKhatiyanDetails', khatiyan.getKhatiyanDetails, name='getKhatiyanDetails'),


    path('getStaffKhatiyanList', staff.getStaffKhatiyanList,
         name='getStaffKhatiyanList'),
         
    path('getStaffList', staff.getStaffList,
         name='getStaffList'),

    path('getKhatiyanDetailsStaff', staff.getKhatiyanDetailsStaff,
         name='getKhatiyanDetailsStaff'),
    path('getProfileDetailsStaff', staff.getProfileDetailsStaff,
         name='getProfileDetailsStaff'),

    path('createProduct', products.createProduct, name='createProduct'),
    path('addProduct', products.addProduct, name='addProduct'),
    path('getProductsList', products.getProductsList, name='getProductsList'),
    path('getProductsSizeList', products.getProductsSizeList,
         name='getProductsSizeList'),
    path('getProductProductionDetails', products.getProductProductionDetails,
         name='getProductProductionDetails'),
    path('getProductsSizeList', products.getProductsSizeList,name='getProductsSizeList'),
    path('getProductsAvailableList', products.getProductsAvailableList,name='getProductsAvailableList'),
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
    path('dailysheetJomaKhorochList', dailySheet.dailysheetJomaKhorochList, name='dailysheetJomaKhorochList'),
    path('getKhorochDataListForUpdate', dailySheet.getKhorochDataListForUpdate, name='getKhorochDataListForUpdate'),
         
    path('getJomaDataList', dailySheet.getJomaDataList,
         name='getJomaDataList'),
    path('getKhorochDataList', dailySheet.getKhorochDataList,
         name='getKhorochDataList'),


    path('createBill', bill.createBill,name='createBill'),
    path('addBillToPartyKhatiyan', bill.addBillToPartyKhatiyan,name='addBillToPartyKhatiyan'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
