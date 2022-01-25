from django.shortcuts import render

# Create your views here.

def gst(request):
    if request.GET:
        a=int(request.GET['user'])
        opt= request.GET['category']

        if opt =='electronics':
            gst =a +a*18/100
            return render(request,'gst.html',{'cat':opt,'ans':gst,'val1':a})
        elif opt =='grocery':
            gst =a +a*10/100
            return render(request,'gst.html',{'cat':opt,'ans':gst,'val1':a})
        elif opt=='furniture':
            gst=a+a*5/100
            return render(request,'gst.html',{'cat':opt,'ans':gst,'val1':a})

    return render(request,'gst.html')                
