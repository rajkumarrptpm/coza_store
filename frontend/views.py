from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from backend.models import productdb, categorydb, branddb, sizedb, contact_us_db
from frontend.models import registerdb
from backend import templates


# Create your views here.
def homefctn(request,):
    data1 = productdb.objects.all()
    data2 = categorydb.objects.all()
    data3 = branddb.objects.all()
    data4 = sizedb.objects.all()
    context={
            'data1': data1,
             'data2': data2,
             'data3': data3,
             'data4':data4,

             }
    return render(request, "home.html",context )


def contact_fctn(request):
    data1 = productdb.objects.all()
    data2 = categorydb.objects.all()
    data3 = branddb.objects.all()
    data4 = sizedb.objects.all()
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,

    }
    return render(request,"contact.html",context)


def product_fctn(request):
    data1 = productdb.objects.all()
    data2 = categorydb.objects.all()
    data3 = branddb.objects.all()
    data4 = sizedb.objects.all()
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,

    }

    return render(request, "product.html",context)


def about_fctn(request):
    data1 = productdb.objects.all()
    data2 = categorydb.objects.all()
    data3 = branddb.objects.all()
    data4 = sizedb.objects.all()
    context = {
        'data1': data1,
        'data2': data2,
        'data3': data3,
        'data4': data4,

    }
    return render(request, "about.html",context)


def shop_fctn(request):
    data2 = categorydb.objects.all()
    return render(request,"product.html",{'data2':data2})



def disctgryfctn(request,itemctgry):

    print("===itemctgry===",itemctgry)
    data=categorydb.objects.all()
    data2 = categorydb.objects.all()
    catgry=itemctgry.upper()
    products=productdb.objects.filter(add_pdt_category=itemctgry)
    context={
        'products':products,
        'catgry': catgry,
        'data2':data2,
        'data':data,
    }
    return render(request,"product_category.html",context)



def prdt_dtls_fctn(request,dataid):
    data3 = categorydb.objects.all()
    if request.method == "POST":
        data=productdb.objects.get(id=dataid)
        data2 = categorydb.objects.all()
        context={

            'data':data,
            'data2':data2,
            'data3':data3,
        }
    return render(request,"product_details.html",context)

def cart_fctn(request):
    return render(request,"cart.html")







def dis_brand_fctn(request,itembrnd):
    data2 = categorydb.objects.all()

    print("===itembrnd===",itembrnd)
    data1 = categorydb.objects.all()
    data3 = branddb.objects.all()
    brnd=itembrnd.upper()
    products=productdb.objects.filter(add_pdt_brand=itembrnd)
    context={
        'products':products,
        'brnd': brnd,
        'data3':data3,
        'data1':data1,
        'data2':data2,

    }
    return render(request,"prodect_brand.html",context)


def userloginfctn(request):
    data2 = categorydb.objects.all()

    return render(request,'login&reg.html',{'data2':data2})



def reg_data(request):
    if request.method == "POST":
        Full_name=request.POST.get('fullname')
        username=request.POST.get('Username')
        mobile_number=request.POST.get('mobile_number')
        Email=request.POST.get('Email')
        Password=request.POST.get('Password')
        confirmPassword=request.POST.get('confirmPassword')
        if Password==confirmPassword:
            obj=registerdb(full_name=Full_name,username=username,mobile_number=mobile_number,Email=Email,password=Password,repassword=confirmPassword)
            obj.save()
            return render(request,'login&reg.html',{"msg":"registered successfully"})


        else:
            return render(request,"login&reg.html",{"msg":"sorry.....password is not matched"})





def login_dtls_fctn(request):
    if request.method=="POST":
        u_name=request.POST.get('Username')
        password=request.POST.get('Password')
        if registerdb.objects.filter(username=u_name,password=password).exists():
            request.session['Username']=u_name
            request.session['Password']=password
            return render(request, "login&reg.html", {'msg1': 'Login successfully'})

        else:
            return render(request,"login&reg.html",{'msg1':'Invalid User'})


def logout_fctn1(request):
    del request.session['Username']
    del request.session['Password']

    return redirect(homefctn)


def save_contact_us_fctn(request):
    if request.method == "POST":
        cdt_name = request.POST.get('name')
        cdt_email = request.POST.get('email')
        cdt_message = request.POST.get('msg')
        obj = contact_us_db(contact_name=cdt_name, contact_email=cdt_email,contact_message=cdt_message)
        obj.save()
        return redirect(contact_fctn)







