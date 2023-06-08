from django.shortcuts import render, redirect
from .models import Register
from admins1.models import Products
from .models import Purchase
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')


def reg(request):
    if request.method == "POST":
        CNAME = request.POST.get('name')
        CEMAIL = request.POST.get('email')
        CPASSWORD = request.POST.get('password')
        CMOBILE = request.POST.get('mobile')
        CADDRESS = request.POST.get('address')
        CPINCODE = request.POST.get('pincode')
        data = Register(
            cname=CNAME,
            cemail=CEMAIL,
            cpassword=CPASSWORD,
            cmobile=CMOBILE,
            caddress=CADDRESS,
            cpincode=CPINCODE
        )
        data.save()
        return render(request, 'index.html')
    else:
        return render(request, 'reg.html')


def log(request):
    if request.method == "POST":
        try:
            Email = request.POST.get('email')
            Password = request.POST.get('password')
            data = Register.objects.get(cemail=Email, cpassword=Password)
            request.session['userid'] = data.cemail
            print(data)

            return render(request, 'u_home.html')
        except Exception as err:
            print("exception is:", err)
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def home(request):
    return render(request, 'u_home.html')


def profile(request):
    try:
        uid = request.session['userid']
        print(uid)
        data = Register.objects.get(cemail=uid)
        return render(request, 'profile.html', {'profile': [data]})
    except Exception as E:
        print("exception is:", E)
        return render(request, 'u_home.html')


def products(request):
    data = Products.objects.all()
    return render(request, 'u_product.html', {'products': data})


def buyproduct(request, id):
    if request.method == 'POST':
        uid = request.session['userid']
        cid = Register.objects.get(cemail=uid)

        product = Products.objects.get(id=id)
        data = Purchase(
            pname=product.pname,
            pcost=product.pcat,
            pcat=product.pcat,
            pquality=product.pquality,
            pdec=product.pdec,
            cid_id=cid.id,
            pid_id=id
        )
        data.save()
        messages.success(request, 'PURCHASED SUCCESSFULLY')
        return render(request, 'u_product.html')
    else:
        messages.error(request, 'NOT PURCHASED>>CHECK IT')
        return redirect('products', id=id)


def purchase(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request, 'u_purchase.html', {'data': data, 'cdata': cdata})


def lastview(request):
    uid = request.session['userid']
    cdata = Register.objects.get(cemail=uid)
    cid = cdata.id
    data = Purchase.objects.filter(cid_id=cid)
    return render(request, 'lastview.html', {'view': data, 'cdata': cdata})


def logout(request):
    return render(request, 'index.html')
