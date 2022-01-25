from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from .models import Product,Member,tab, time,category
from django.db.models import Q
from .forms import memberform
from .forms import OrderForm
import smtplib, ssl
import random


def login(request):
    if request.method == 'POST':
        try:
            e = request.POST['email']
            request.session['email']=e
            p = request.POST['password']
            x = Member.objects.get(email=e)

            if x.password == p:
                return redirect('home')
            else:
                return HttpResponse("Wrong Password")
        except:
            return HttpResponse("Wrong Username")
    return render(request,'login.html')

def registernew(request):
    a=memberform(request.POST)
    if a.is_valid():
        a.save()
        
    return render(request,'registernew.html',{'form':a})


def pro_add(request):
    a=OrderForm(request.POST or None)
    if a.is_valid():
        a.save()
        return redirect('order')
    return render(request,'pro_add.html',{'form':a})


    

def home(request):
    if request.session.has_key('email'):
        user1 = request.session['email']
        print(user1)
        per = Member.objects.get(email=user1)
        print(per.email)
    return render(request,'index.html' ,{'per':per})
    
def about(request):
    if request.session.has_key('email'): 
        a= Product.objects.all()
    else:
        return redirect('login')
    return render(request,'about.html',{'xyz':a})

def menu(request):
    a=Product.objects.all()
    cat= category.objects.all()
    s = request.GET.get('search')
    if s:
        q= Product.objects.filter(Q(name__icontains = s))
    else:
        q = Product.objects.all()   
           
    return render(request,'menu.html',{'xyz':a,'arshad':cat,'s':q})
    
def contact(request):
    return render(request,'contact.html')    


def register(request):
    if request.method == 'POST':
        obj=Member()
        obj.username=request.POST['username']
        obj.email=request.POST['email']
        obj.password=request.POST['password']
        obj.phone=request.POST['phone']
        obj.save()
    return render(request,'register.html')    
    
def table(request):
    a=tab.objects.filter(status = True)
    if request.method == 'POST':
        obj=time()
        obj.date=request.POST['date']
        obj.save()
    return render(request,'table.html',{'xyz':a})

def date(request):
    return render(request,'date.html')
 
    

def catwise(request,name):
    cat = category.objects.get(name=name)
    cate = category.objects.all()
    product = Product.objects.all().filter(category=cat)
    return render(request,'catwise.html',{'cat':cat,'arshad': cate ,'pro':product})

def productview(request,pk):
    view = get_object_or_404(Product,pk=pk)
    return render(request,'productview.html',{'v':view})


def order(request):
    order=Product.objects.all()
    return render(request,'order.html',{'ord':order})

def forgotpass(request):
    email = request.POST.get('email')
    request.session['email'] = email
    if email == None:
        return render(request,'email.html')

        
    print(email)
    otpcheck = ''
    rand = random.choice('0123456789')
    rand1 = random.choice('0123456789')
    rand2 = random.choice('0123456789')
    rand3 = random.choice('0123456789')
    otpcheck = rand + rand1 + rand2 + rand3
    print(otpcheck)
    request.session['otpcheck'] = otpcheck
    
    port = 465
    password = "Arshad786."
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp.gmail.com",port,context=context)
    server.login("arshadmiya34@gmail.com",password)
    server.sendmail("rushansaiyed5884@gmail.com",email,otpcheck)
    server.quit()
    return redirect('otpcheck')

   
 
   

def otpcheck(request):
     if request.session.has_key('otpcheck'):
        otpcheck = request.session['otpcheck']
        try:
            otpcheckobj = request.POST.get('otpcheck')
            if otpcheckobj == None:
                return render(request,'otpcheck.html')
            if otpcheck == request.POST.get('otpcheck'):
                return redirect('newpassword')
            else:
                return HttpResponse("<a href = ''>Wrong OTP Entered.</a>")
        except:
            return redirect('login')
     return render(request,'otpcheck.html')

def newpassword(request):
    newpassword = request.POST.get('password')
    if newpassword == None:
        return render(request,'forgotpass.html')
    obj = Member.objects.get(email = request.session['email'])
    obj.password = newpassword
    obj.save()
    return redirect('login')


def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    return redirect('login')

def edit(request):
    if request.session.has_key('email'):
            profile = Member.objects.get(email=request.session['email'])
            if request.method == 'POST':
                profile.username = request.POST['username'] or None
                profile.email = request.POST['email'] or None
                profile.phone = request.POST['phone'] or None
                profile.password = request.POST['password'] or None
                profile.save()
                return redirect('login')
    return render(request,'edit.html',{'profile':profile}) 




    
# def mainProduct(request):
#     obj1 = product.objects.all()
#     s = request.GET.get('search')
#     if s:
#         q= product.objects.filter(Q(name__icontains = s) | Q(des__icontains= s ))
#     else:
#         q = product.objects.all()
#     return render(request, 'new.html', {'mainProd': obj1, 's' : q})    
    
# Create your views here.

