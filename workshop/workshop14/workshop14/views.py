from django.shortcuts import render



def info(request):
    return render(request,"info.html")

def student(request,name):
    a={'홍길동':28,'김길동':26,'박길동':14}
    b=a.get(name)
    
    return render(request,"student.html",{'name':name,'b':b})