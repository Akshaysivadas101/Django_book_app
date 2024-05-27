from django.shortcuts import render,redirect
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from book_app.models import Book
from .models import Cart,CartItem

def listBook(request):
    books = Book.objects.all()
    paginator= Paginator(books,4)
    page_number= request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'user/userlistbook.html',{'books':books,'page':page})

def Search_book(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render(request,'user/usersearch.html',context)

def detailsView(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'user/userdetailsview.html',{'book':book})

def add_to_cart(request,book_id):
    book=Book.objects.get(id=book_id)
    if book.quantity>0:
        cart,created=Cart.objects.get_or_create(user=request.user)
        cart_item,item_created=CartItem.objects.get_or_create(cart=cart,book=book)
        if not item_created:
            cart_item.quantity+=1
            cart_item.save()
    return redirect('addtocart')

def view_cart(request):
    cart,created=Cart.objects.get_or_create(user=request.user)
    cart_items= cart.cart_item_set.all()
    cart_item= CartItem.objects.all()
    total_price=sum(item.book.price * item.quantity for item in cart_items)
    total_items=cart_items.count()

    context={'cart_items':cart_items,'cart_item':cart_item,'total_price':total_price,'total_items':total_items}
    return render(request,'cart.html',context)

def increase_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity < cart_item.book.quantity:
        cart_item.quantity+=1
        cart_item.save()
    return redirect(request,'addtocart')

def decrease_quantity(request,item_id):
    cart_item=CartItem.objects.get(id=item_id)
    if cart_item.quantity<cart_item.book.quantity:
        cart_item.quantity-=1
        cart_item.save()
    return redirect(request,'addtocart')

def remove_from_cart(request,item_id):
    try:
        cart_item=CartItem.objects.get(id=item_id)
        cart_item.delete()
    except cart_item.DoesNotExist:
        pass
    return redirect(request,'addtocart')








