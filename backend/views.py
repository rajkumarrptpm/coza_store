from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from backend.models import categorydb, productdb, branddb, sizedb, contact_us_db


# Create your views here.

def indexfctn(request):
    return render(request,"index.html")



#category functions
def add_category_fctn(request):
    return render(request,"add_category.html")


def display_category_fctn(request):
    data = categorydb.objects.all()
    return render(request, "display_category.html", {'data': data})


def save_category_fctn(request):
    if request.method == "POST":
        ctgry_name = request.POST.get('ct_name')
        ctgry_dsc = request.POST.get('ct_discription')
        ctgry_img = request.FILES['ct_image']
        obj = categorydb(add_ct_name=ctgry_name, add_ct_dsc=ctgry_dsc, add_ct_profile=ctgry_img)
        obj.save()
        return redirect(indexfctn)


def edit_category_fctn(request, dataid):
    data = categorydb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_category.html", {'data': data})


def Update_category_fctn(request, dataid):
   if request.method == "POST":
        ctgry_name = request.POST.get('ct_name')
        ctgry_dsc = request.POST.get('ct_discription')
        try:
            img = request.FILES['ct_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=dataid).add_ct_profile
        categorydb.objects.filter(id=dataid).update(add_ct_name=ctgry_name, add_ct_dsc=ctgry_dsc, add_ct_profile=file)
        return redirect(display_category_fctn)


def delete_category_fctn(request, dataid):
    data = categorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_category_fctn)







#product functions

def add_product_fctn(request):
    data = categorydb.objects.all()
    data1 = branddb.objects.all()
    data2 = sizedb.objects.all()

    return render(request, "add_product.html", {'data': data, 'data1': data1 , 'data2':data2})


def display_product_fctn(request):
    data = productdb.objects.all()
    return render(request, "display_product.html", {'data': data})


def save_add_product_fctn(request):
    if request.method == "POST":
        prdt_ctgry = request.POST.get('pd_category')
        prdt_brnd = request.POST.get('pd_brand')
        prdt_name = request.POST.get('pd_name')
        prdt_dsc = request.POST.get('pd_discription')
        prdt_size = request.POST.get('pd_size')
        prdt_price = request.POST.get('pd_price')
        prdt_img_1 = request.FILES['pd_image_1']
        prdt_img_2 = request.FILES['pd_image_2']
        prdt_img_3 = request.FILES['pd_image_3']

        obj = productdb(add_pdt_category=prdt_ctgry,add_pdt_brand=prdt_brnd, add_pdt_name=prdt_name, add_pdt_dsc=prdt_dsc,
                        add_pdt_size=prdt_size, add_pdt_price=prdt_price, add_pdt_profile_1=prdt_img_1,add_pdt_profile_2=prdt_img_2,add_pdt_profile_3=prdt_img_3)
        obj.save()
        return redirect(indexfctn)


def edit_product_fctn(request, dataid):
    data = productdb.objects.get(id=dataid)
    data1 = categorydb.objects.all()
    data2 = sizedb.objects.all()
    data3 = branddb.objects.all()
    context={

        'data': data,
        'data2': data2,
        'data1':data1,
        'data3':data3,
    }

    return render(request, "edit_product.html",context)


def Update_product_fctn(request, dataid):
    if request.method == "POST":
        prdt_ctgry = request.POST.get('pd_category')
        prdt_brnd = request.POST.get('pd_brand')
        prdt_name = request.POST.get('pd_name')
        prdt_dsc = request.POST.get('pd_discription')
        prdt_size = request.POST.get('pd_size')
        prdt_price = request.POST.get('pd_price')

        try:
            img = request.FILES['pd_image_1']
            fs = FileSystemStorage()
            file_1 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file_1 = productdb.objects.get(id=dataid).add_pdt_profile_1

        try:
            img = request.FILES['pd_image_2']
            fs = FileSystemStorage()
            file_2 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file_2 = productdb.objects.get(id=dataid).add_pdt_profile_2

        try:
            img = request.FILES['pd_image_3']
            fs = FileSystemStorage()
            file_3 = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file_3 = productdb.objects.get(id=dataid).add_pdt_profile_3


        productdb.objects.filter(id=dataid).update(add_pdt_category=prdt_ctgry, add_pdt_brand=prdt_brnd, add_pdt_name=prdt_name,
                        add_pdt_dsc=prdt_dsc,
                        add_pdt_size=prdt_size, add_pdt_price=prdt_price, add_pdt_profile_1=file_1,
                        add_pdt_profile_2=file_2, add_pdt_profile_3=file_3)
        return redirect(display_product_fctn)


def delete_prdt_fctn(request, dataid):
    data = productdb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_product_fctn)







#brand function

def add_brand_fctn(request):
    return render(request,"add_brand.html")


def display_brand_fctn(request):
    data = branddb.objects.all()
    return render(request, "display_brand.html", {'data': data})


def save_brand_fctn(request):
    if request.method == "POST":
        brnd_name = request.POST.get('bd_name')
        brnd_dsc = request.POST.get('bd_discription')
        brnd_img = request.FILES['bd_image']
        obj = branddb(add_bd_name=brnd_name, add_bd_dsc=brnd_dsc, add_bd_profile=brnd_img)
        obj.save()
        return redirect(indexfctn)


def edit_brand_fctn(request, dataid):
    data = branddb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_brand.html", {'data': data})


def Update_brand_fctn(request, dataid):
   if request.method == "POST":
        brnd_name = request.POST.get('bd_name')
        brnd_dsc = request.POST.get('bd_discription')
        try:
            img = request.FILES['bd_image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = branddb.objects.get(id=dataid).add_bd_profile
        branddb.objects.filter(id=dataid).update(add_bd_name=brnd_name, add_bd_dsc=brnd_dsc, add_bd_profile=file)
        return redirect(display_brand_fctn)


def delete_brand_fctn(request, dataid):
    data = branddb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_brand_fctn)






#size function


def add_size_fctn(request):
    return render(request,"add_size.html")


def display_size_fctn(request):
    data = sizedb.objects.all()
    return render(request, "display_size.html", {'data': data})


def save_size_fctn(request):
    if request.method == "POST":
        size_ltr = request.POST.get('sz_letters')
        size_num = request.POST.get('sz_numbers')

        obj = sizedb(size_ltr=size_ltr, size_num=size_num)
        obj.save()
        return redirect(indexfctn)


def edit_size_fctn(request, dataid):
    data = sizedb.objects.get(id=dataid)
    print(data)
    return render(request, "edit_size.html", {'data': data})


def Update_size_fctn(request, dataid):
   if request.method == "POST":
        size_ltr = request.POST.get('sz_letters')
        size_num = request.POST.get('sz_numbers')

        sizedb.objects.filter(id=dataid).update(size_ltr=size_ltr, size_num=size_num)
        return redirect(display_size_fctn)


def delete_size_fctn(request, dataid):
    data = sizedb.objects.filter(id=dataid)
    data.delete()
    return redirect(display_size_fctn)




def loginfctn(request):
    return render(request,"login.html")


def addloginfctn(request):
    if request.method == "POST":

        usrname=request.POST.get('username')
        pswrd=request.POST.get('password')

        if User.objects.filter(username__contains=usrname).exists():
            user=authenticate(username=usrname,password=pswrd)
            if user is not None:
                login(request,user)
                request.session['username']=usrname
                request.session['password']=pswrd
                return redirect(indexfctn)
            else:
                return redirect(loginfctn)
        else:
            return redirect(loginfctn)


def logout_fctn(request):
    del request.session['username']
    del request.session['password']

    return redirect(loginfctn)



def Messagefctn(request):
    data=contact_us_db.objects.all()
    return render(request,"messages.html",{'data':data})


