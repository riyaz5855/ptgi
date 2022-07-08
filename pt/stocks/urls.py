from stocks import views
from django.urls import path

urlpatterns = [
    path('login/',views.ulogin,name='ulogin'),
    path('logout/',views.ulogout,name='ulogout'),
    path('', views.addshow,name='addshow'),
    path('delte/<int:id>/',views.deletedata,name='deletedata'),
    path('delteindi/<str:maker>/<int:id>/',views.deleteindi,name='deleteindi'),
    path('update/<int:id>/',views.updatedata,name='updatedata'),
    path('updateindi/<str:maker>/<int:id>/',views.updateindi,name='updateindi'),
    path('search/', views.search,name='search'),
    path('advsearch/', views.advsearch,name='advsearch'),
    
    # admin add and show
    path('addandshow/<str:maker>/', views.maker,name='addandshow'),

    # maker table
    path('makertable/<str:maker>/', views.maker_table,name='makertable'),
    
    # maker edit
    path('makeredit/<str:maker>/<int:id>/', views.maker_edit,name='makeredit'),

    # admin received table
    path('adminrec/<str:maker>/', views.admin_rec,name='adminrec'),
    
    # admin received edit
    path('adminrecedit/<str:maker>/<int:id>/', views.admin_rec_edit,name='adminrecedit'),

    # Reject cutting
    path('reject/<str:maker>/<int:id>/',views.reject_cutting,name='rejectcutting'),

    # hisab
    path('hsbclr/<str:maker>/', views.hsbclr ,name='hsbclr'),

    # hisab clear
    path('hisabclear/<str:maker>/<int:frm>/<int:to>/', views.clrr, name='hisabclear'),
   
    # clear Stock
    path('clrstk/',views.clrstk, name='clrstk'),

    # item edit
    path('itemedit/',views.itemedit, name='itemedit'),
    path('itemdelete/<int:id>/',views.itemdelete, name='itemdelete'),
    path('itemupdate/<int:id>/',views.itemupdate, name='itemupdate'),
]   
