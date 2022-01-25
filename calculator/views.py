from django.shortcuts import render

# Create your views here.


def calculator(request):
    if request.POST:
        val1 = request.POST['a1']
        val2 = request.POST['a2']
        opt1 = request.POST['a3']
        if opt1 == 'sum':
            var = float(val1) + float(val2)
            return render(request,'calculator.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == 'minus':
            var = float(val1) - float(val2)
            return render(request,'calculator.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == 'multi':
            var = float(val1) * float(val2)
            return render(request,'calculator.html',{'ans':var,'val1':val1,'val2':val2})

        elif opt1 == 'division':
            var = float(val1) / float(val2)
            return render(request,'calculator.html',{'ans':var,'val1':val1,'val2':val2})
            
    return render(request,'calculator.html')