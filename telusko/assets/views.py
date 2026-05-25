from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"index.html",)
 
# def prime(request):
#     val1=int(request.GET['num1'])
#     # val2=int(request.GET['num2' ])
#     # res=val1-val2
#     for i in range(2,val1):
#         if val1%i ==0:
#             return render(request,"result.html",{'result':False})
          
#     else:
#         return render(request,"result.html",{'result':True})
