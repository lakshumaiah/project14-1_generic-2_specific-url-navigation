from django.shortcuts import render

# Create your views here.
def gen_fun(request):
    return render(request,'gen_fun.html')