from datetime import datetime
from django.shortcuts import render,HttpResponse
from .models import Contact

# Create your views here.

# def home(request):
#     return render(request,"index.html",{})

# def view_emp(request):
#     emps= Contact.objects.all()
#     data={
#         'emps':emps,
#     }
#     return render(request,"view.html",data)


def view_contact(request):
    if request.method=='GET':
        resp=render(request,"contact.html")
        return resp
    elif request.method=='POST':
        if 'add' in request.POST:
            con=Contact()
            con.name= request.POST.get('name','na')
            con.email= request.POST.get('email','na')
            con.desc= request.POST.get('desc','na')
            con.save()
            return HttpResponse("DATA INSERTED")

        elif 'search' in request.POST:
            eid=int(request.POST.get('texteid',0))
            emp= Contact.objects.get(id=eid)
            d1={'emp':emp}
            resp= render(request,'contact.html',context=d1)
            return resp

        elif 'update' in request.POST:
            con=Contact()
            con.id=int(request.POST.get('texteid',0))
            if Contact.objects.filter(id=con.id).exists():
                con.name= request.POST.get('name','na')
                con.email= request.POST.get('email','na')
                con.desc= request.POST.get('desc','na')
                con.save()
            return HttpResponse("DATA UPDATED SUCCESSFULLY!!")

        elif 'delete' in request.POST:
            eid=(request.POST.get('texteid',0))
            Contact.objects.filter(id=eid).delete()
            return HttpResponse("DATA DELETED SUCCESSFULLY!!") 
        elif 'show' in request.POST:
            allemp=Contact.objects.all()
            d1={'employee': allemp}
            resp= render(request,'contact.html',context=d1)
            return resp


