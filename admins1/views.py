from django.shortcuts import render

from .models import Products
from users1.models import Purchase
from users1.models import Register

from PIL import Image
from django.core.files import File


def alogin(request):
    if request.method == 'POST':
        try:
            aemail = request.POST.get('aemail')
            apassword = request.POST.get('apassword')
            if aemail == 'bhavyalatha4444@gmail.com' and apassword == '4444':
                return render(request, 'a_home.html')
            else:
                return render(request, 'a_login.html')
        except Exception as err:
            print("EXCEPTION IS:", err)
            return render(request, 'a_login.html')
    else:
        return render(request, 'a_login.html')


def addproduct(request):
    if request.method == 'POST':
        try:
            pname = request.POST.get('pname')
            pcat = request.POST.get('pcat')
            pcost = request.POST.get('pcost')
            pquality = request.POST.get('pquality')
            pdec = request.POST.get('pdec')
            pimage = request.FILES['pimage']
            print(pimage)

            data = Products(
                pname=pname,
                pcat=pcat,
                pcost=pcost,
                pquality=pquality,
                pdec=pdec,
                pimage=pimage,
            )
            data.save()
            return render(request, 'a_viewproduct.html')
        except Exception as err:
            print("EXCEPTION is:", err)
            return render(request, 'a_home.html')
    else:
        return render(request, 'a_addproduct.html')


def viewproduct(request):
    data = Products.objects.all()
    print(data)
    return render(request, 'a_viewproduct.html', {'data': data})


def ahome(request):
    return render(request, 'a_home.html')


def profile1(request):
    try:
        data = Products.objects.all()
        return render(request, 'a_viewproduct.html', {'profile4': [data]})
    except Exception as err:
        print("EXCEPTION IS:", err)
        return render(request, 'a_addproduct.html')


def alogout(request):
    return render(request, 'a_home.html')


def alastview(request):
    uid = request.session['userid']
    cdata = Register.objects.all()
    cid = cdata
    data = Purchase.objects.all()
    return render(request, 'alastview.html',{'view': data, 'cdata': cdata})
