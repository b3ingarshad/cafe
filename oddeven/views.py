from django.shortcuts import render

# Create your views here.

def oddeven(request):
    if request.GET:
        a=int(request.GET['user'])
        

        
        if(a%2) == 0:
            even = f"{a} is even"
            return render(request,'oddeven.html',{'cat':a,'ans':even})
        else:
            odd = f"{a} is odd"
            return render(request,'oddeven.html',{'cat':a,'ans':odd})
         
    return render(request,'oddeven.html')
