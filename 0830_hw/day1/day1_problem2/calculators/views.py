from django.shortcuts import render

# Create your views here.
def calculate(request):
    return render(request, 'calculate.html')

def result(request):
    first = request.GET.get('first')
    second = request.GET.get('second')
    menus = ["짜장면","짬뽕","치킨","피자"]
    context = {
        'first':first,
        'second':second,
        'menus':menus,
    }
    return render(request, 'result.html', context)