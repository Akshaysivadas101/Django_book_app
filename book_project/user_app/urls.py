from django.urls import path
from . import views
#
urlpatterns = [



    path('',views.listBook,name='book-list'),
    path('details/<int:book_id>/',views.detailsView,name='userdetails'),
    path('search/',views.Search_book,name='usersearch'),
     path('add_to_cart/<int:book_id>/',views.add_to_cart,name="addtocart"),
     path('view-cart/',views.view_cart,name='viewcart'),
     path('increase/<int:item_id>/',views.increase_quantity,name='increase_quantity'),
     path('decrease/<int:item_id>/',views.decrease_quantity,name='decrease_quantity')
]