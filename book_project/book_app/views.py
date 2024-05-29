from django.shortcuts import render,redirect
from .models import Book,Author
from .forms import *
from django.core.paginator import Paginator,EmptyPage
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


#def createBook(request):
    # books = Book.objects.all()
    # if request.method == 'POST':
    #     title = request.POST.get('title')
    #     price = request.POST.get('price')
    #     book = Book(title=title, price=price)
    #     book.save()
    # return render(request,'book.html',{'books':books})

def detailsView(request,book_id):
    book = Book.objects.get(id=book_id)
    return render(request,'admin/detailsview.html',{'book':book})

# def updateBook(request,book_id):
#     book = Book.objects.get(id=book_id)
#     if request.method == 'POST':
#         title = request.POST.get('title')
#         price = request.POST.get('price')
#
#         book.title=title
#         book.price=price
#         book.save()
#         return redirect('/')
#     return render(request,'updateview.html',{'book':book})

def deleteview(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('home')
    return render(request,'admin/deleteview.html',{'book':book})



def createBook(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request,'admin/book.html',{'form':form,'books':books})

def Create_Author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AuthorForm()
    return render(request,'admin/author.html',{'form':form})

def updateBook(request,book_id):
    book = Book.objects.get(id=book_id)
    if request.method == 'POST':
        form = BookForm(request.POST,request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)
    return render(request,'admin/updateview.html',{'form':form})

def index(request):
    return render(request,'admin/index.html')

def listBook(request):
    books = Book.objects.all()
    paginator= Paginator(books,4)
    page_number= request.GET.get('page')
    try:
        page=paginator.get_page(page_number)
    except EmptyPage:
        page=paginator.page(page_number.num_pages)
    return render(request,'admin/listbook.html',{'books':books,'page':page})


def Search_book(request):
    query=None
    books=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        books=Book.objects.filter(Q(title__icontains=query))
    else:
        books=[]
    context={'books':books,'query':query}
    return render(request,'admin/search.html',context)

# def Register_user(request):
#     if request.method =='POST':
#         username = request.POST.get('username')
#         first_name = request.POST.get('first_name')
#         email = request.POST.get('email')
#         last_name = request.POST.get('last_name')
#         password = request.POST.get('password')
#         cpassword = request.POST.get('password1')
#         if password==cpassword:
#             if User.objects.filter(username=username).exists():
#                 messages.info(request,'This username already exists')
#                 return redirect('register')
#             elif User.objects.filter(email=email).exists():
#                 messages.info(request,'This mail id is already registered')
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
#                 user.save()
#             return redirect('login')
#         else:
#             messages.info(request,'The password are not matching')
#             return redirect('register')
#     return render(request,'register.html')
#
# def loginPage(request):
#     if request.method =='POST':
#         username = request.POST('username')
#         password = request.POST('password')
#         user=loginTable.objects.filter(username=username,password=password,type='user').exists()
#         try:
#             if user is not None:
#                 user_details=loginTable.objects.get(username=username,password=password)
#                 user_name=user_details.username
#                 type=user_details.type
#
#                 if type=='user':
#                     request.session['username']= user_name
#                     return redirect('user_view')
#                 elif type=='admin':
#                     request.session['username']=user_name
#                     return redirect('admin_view')
#             else:
#                 messages.error(request,'Invalid username or password')
#         except:
#             messages.error(request,'Invalid role')
#     return render(request,'login.html')

def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            raw_password= form.cleaned_data.get('password1')
            user=authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('/')
    else:
        form = RegisterForm()
    return render(request,'admin/register.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('admin/login')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request,request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home/')
    else:
        form = LoginForm()




    return render(request, 'admin/login.html', {'form': form})















