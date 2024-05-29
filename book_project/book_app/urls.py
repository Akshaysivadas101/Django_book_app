
from django.urls import path,include
from . import views

urlpatterns = [
    path('createbook/', views.createBook,name='createbook'),
    path('author/', views.Create_Author,name='author'),
    path('detailsview/<int:book_id>/',views.detailsView,name='details'),
    path('updateview/<int:book_id>/',views.updateBook,name='update'),
    path('deleteview/<int:book_id>/',views.deleteview,name='delete'),
    path('index/',views.index),
    path('home/',views.listBook,name='booklist'),
    path('search/',views.Search_book,name='search'),
    path('',views.user_login,name='user_login'),
    path("register/",views.register, name ='register'),
    path('user/',include('user_app.urls'))

]
