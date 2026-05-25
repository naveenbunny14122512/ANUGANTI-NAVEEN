from django.shortcuts import render
from .models import Student

# Create your views here.
# def good(request):
#         if request.method =='POST':
#             name=request.POST.get('Name')
#             return render(request,"1412.html",{"Name":name})
#         else:
#             return render(request,"1412.html")
# def good(request):
#     if request.method == 'POST':
#         name = request.POST.get('first_name')
#         sqaure=request.POST.get('Number')
#         squared_num=pow(int(sqaure),2)
#         return render(request, "1412.html", {"name": name, "square":squared_num})

#     return render(request, "1412.html")
    
    
# def Armstrong(request):
#     if request.method =='POST':
#         Number=request.POST.get('num1')
#         if Number:
#             n_l=str(len(Number))
#             sum_arm=0
#             for i in str(Number):
#                 sum_arm+=pow(int(i),int(n_l))
#             print(sum_arm)
#             if int(Number)==sum_arm:
#                 return render(request,"1412.html",{"Number":True})
#             else:
#                 print(Number)
#                 return render(request,"1412.html",{"Number":False})
#         else:
#             return render(request,"1412.html",{"Error":"Please Enter a number to find an Armstrong number"})
            
#     else:
#         return render(request, "1412.html")


# def Thirdlargest(request):
#     list=[]
#     if request.method =='POST':
#         n1=request.POST.get('num1')
#         list.append(n1)
#         n2=request.POST.get('num2')
#         list.append(n2)
#         n3=request.POST.get('num3')
#         list.append(n3)
#         for i in range(len(list)-1):
#             if list[i]>list[i+1]:
#                 temp=list[i+1]
#                 list[i+1]=list[i]
#                 list[i]=temp
                
#         return render(request,"1412.html",{"Largest":list[0]})
#     else:
#         return render(request,"1412.html")

# def SRS(request):
#     marks=[]
#     if request.method =='POST':
#         name=request.POST.get('Name')
#         if name:
#             m1=request.POST.get('marks1')
#             if m1:
#                 marks.append(int(m1))
#                 m2=request.POST.get('marks2')
#                 if m2:
#                     marks.append(int(m2))
#                     m3=request.POST.get('marks3')
#                     if m3:
#                         marks.append(int(m3))
#                         m4=request.POST.get('marks4')
#                         if m4:
#                             marks.append(int(m4))
#                         else:
#                             return render(request,"1412.html",{"Error":"Please Enter 4th subject Marks "})
#                     else:
#                         return render(request,"1412.html",{"Error":"Please Enter 3rd subject Marks "})
                    
#                 else:
#                     return render(request,"1412.html",{"Error":"Please Enter 2nd Marks "})
#             else:
#                 return render(request,"1412.html",{"Error":"Please Enter 1st Subject Marks"})
#         else:
#             return render(request,"1412.html",{"Error":"Please Enter a your Name"})
        
#         total=sum(marks)
#         total_avg=total/len(marks)
#         if total_avg >= 90:
#             return render(request,"1412.html",{"Name":name,"Grade":"Grade A","total_avg":total_avg})
#         elif total_avg >= 80:
#             return render(request,"1412.html",{"Name":name,"Grade":"Grade B","total_avg":total_avg})
#         elif total_avg >= 80:
#             return render(request,"1412.html",{"Name":name,"Grade":"Grade C","total_avg":total_avg})
#         elif total_avg >= 70:
#             return render(request,"1412.html",{"Name":name,"Grade":"Grade D","total_avg":total_avg})
#         else:
#             return render(request,"1412.html",{"Name":name,"Grade":"Fail","total_avg":total_avg})
#     else:
#         return render(request,"1412.html")

from django.shortcuts import render

def SRS(request):

    if request.method == 'POST':

        name = request.POST.get('Name')
        m1 = request.POST.get('marks1')
        m2 = request.POST.get('marks2')
        m3 = request.POST.get('marks3')
        m4 = request.POST.get('marks4')

        # storing old values for UI refill
        context = {
            "Name": name,
            "m1": m1,
            "m2": m2,
            "m3": m3,
            "m4": m4,
        }

        # validations
        if not name:
            context["Error"] = "Please Enter Your Name"
            return render(request, "1412.html", context)

        if not m1:
            context["Error"] = "Please Enter 1st Subject Marks"
            return render(request, "1412.html", context)

        if not m2:
            context["Error"] = "Please Enter 2nd Subject Marks"
            return render(request, "1412.html", context)

        if not m3:
            context["Error"] = "Please Enter 3rd Subject Marks"
            return render(request, "1412.html", context)

        if not m4:
            context["Error"] = "Please Enter 4th Subject Marks"
            return render(request, "1412.html", context)

        marks = [
            int(m1),
            int(m2),
            int(m3),
            int(m4)
        ]

        total = sum(marks)
        total_avg = total / len(marks)

        # grading
        if total_avg >= 90:
            grade = "Grade A"

        elif total_avg >= 80:
            grade = "Grade B"

        elif total_avg >= 70:
            grade = "Grade C"

        elif total_avg >= 50:
            grade = "Grade D"

        else:
            grade = "Fail"
            
        Student.objects.create(
            Name=name,
            marks1=marks[0],
            marks2=marks[1],
            marks3=marks[2],
            marks4=marks[3],
            total=total,
            total_avg=total_avg,
            Grade=grade
        )
            

        # final result
        context.update({
            "Grade": grade,
            "total": total,
            "total_avg": total_avg
        })

        return render(request, "1412.html", context)

    return render(request, "1412.html")


        
        
        
            
            
    