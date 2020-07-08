from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Owner
from .models import Bill_Categories
from .models import Bill_table
from .forms import OwnerForm
from .forms import Bill_CategoriesForm
from .forms import Bill_tableForm
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from time import time
# Create your views here.


def mainhome(request):
    if request.user.is_authenticated:
        return render(request,'main.html',{'title':'Dashboard'})
    else:
        return redirect("login")


def register(request):

    if request.method == "POST":
        if request.POST['first_name'] and request.POST['last_name'] and request.POST['username'] and request.POST['email'] and request.POST['password1'] and request.POST['password2'] is not None:
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']

            if password1== password2:

                if User.objects.filter(username=username).exists():
                    messages.info(request,'username taken')
                    return render(request,'register.html')

                else:
                
                    if User.objects.filter(email=email).exists():
                        messages.info(request,'email taken')
                        return render(request,'register.html')
                
                    else:
                        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,email=email,password=password1)
                        user.save()
                        return render(request,'login.html')

            else:
                messages.info(request,'password not match')
                return render(request,'register.html')
        else:
            messages.info(request,'fill up full form')
            return render(request,'register.html')


    else:
        return render(request,'register.html')

    


def login(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect("/")

        else:
            messages.info(request,'user name or password wrong')
            return redirect("login")
        

    else:
        return render(request,"login.html")
        


def logout(request):
    auth.logout(request)
    return redirect("login")



def createLandowner(request):

    if request.user.is_authenticated:
        
        if request.method == "POST":

            if request.POST['name'] and request.POST['email'] and request.POST['contact'] and request.POST['address'] is not None:

                name = request.POST['name']
                email = request.POST['email']
                contact = request.POST['contact']
                address = request.POST['address']
                user_id = request.user.id
                user = Owner(name=name,email=email,contact=contact,address=address,user_id=user_id)
                user.save()
                owner = Owner.objects.filter(user_id=request.user.id)
                contex ={
                    'owner': owner,
                }

                return redirect("landowner")

            else:
                return render(request,'createland.html',{'title':'Create Landowner'})

    
        else:
            return render(request,'createland.html',{'title':'Create Landowner'})

    else:
        return redirect("login")


    


def landowner(request):
    if request.user.is_authenticated:
        owner = Owner.objects.filter(user_id=request.user.id)
    
        contex={
            'owner': owner,
            'title':'Landowner List',
        }
        return render(request,'showland.html',contex)

    else:
        return redirect("login")
    



def deleteLandowner(request,nid):
    if request.user.is_authenticated:
        instance= get_object_or_404(Owner,id=nid)
        instance.delete()

        '''owner = Owner.objects.filter(user_id=request.user.id)
        print(owner)
        contex = {
            'nid': nid,
            'owner': owner,
        }
        return render(request,'reshow.html',contex)'''

        return redirect("landowner")

    else:
        return redirect("login")




def editLandowner(request,nid): 
    if request.user.is_authenticated:

        instance= get_object_or_404(Owner,id=nid)
        form= OwnerForm(request.POST or None, instance=instance)
        
        if form .is_valid():
            instance= form.save(commit=False)
            instance.save()
            return redirect("landowner")
    
        contex={
        'form':form,
        'instance':instance,
        'title':'Edit Landowner',
        }
        return render(request,'update.html',contex)
    else:
        return redirect("login")


def bill_categories(request):
    if request.user.is_authenticated:
        bill_categories = Bill_Categories.objects.filter(user_id=request.user.id)
    
        contex={
            'bill_categories': bill_categories,
            'title':'Bill Category List',
        }
        return render(request,'show_bill_category.html',contex)

    else:
        return redirect("login")


def createBill_Categories(request):
    if request.user.is_authenticated:
        
        if request.method == "POST":

            if request.POST['name'] and request.POST['color'] and request.FILES['icon'] is not None:

                name = request.POST['name']
                color = request.POST['color']
                user_id = request.user.id
                icon = request.FILES['icon']
                billCatagory = Bill_Categories(name=name,color=color,user_id=user_id,icon=icon)
                billCatagory.save()
                bill_categories = Bill_Categories.objects.filter(user_id=request.user.id)
                contex ={
                    'bill_categories': bill_categories,
                }

                return redirect("bill_categories")

            else:
                return render(request,'create_bill_category.html',{'title':'Create Bill Category'})

    
        else:
            return render(request,'create_bill_category.html',{'title':'Create Bill Category'})

    else:
        return redirect("login")



def editBill_categories(request,nid): 
    if request.user.is_authenticated:

        instance= get_object_or_404(Bill_Categories,id=nid)
        form= Bill_CategoriesForm(request.POST or None, instance=instance)
        
        if form .is_valid():
            instance= form.save(commit=False)
            instance.save()
            return redirect("bill_categories")
    
        contex={
        'form':form,
        'instance':instance,
        'title':'Update Bill Category',
        }
        return render(request,'update_bill_category.html',contex)
    else:
        return redirect("login")




def deleteBill_categories(request,nid):
    if request.user.is_authenticated:
        instance= get_object_or_404(Bill_Categories,id=nid)
        instance.delete()

        '''owner = Owner.objects.filter(user_id=request.user.id)
        print(owner)
        contex = {
            'nid': nid,
            'owner': owner,
        }
        return render(request,'reshow.html',contex)'''

        return redirect("bill_categories")

    else:
        return redirect("login")




def bills(request):
    if request.user.is_authenticated:
        timestamp= 1424197820
        
        print(datetime.fromtimestamp(timestamp))
        bills = Bill_table.objects.filter(created_by=request.user.id)
        owner = Owner.objects.all()
        bill_categories = Bill_Categories.objects.all()
        contex={
            'bills': bills,
            'owner':owner,
            'bill_categories':bill_categories,
            'title':'Bill Category List',
            'timestamp':timestamp,
        }
        return render(request,'show_bills.html',contex)

    else:
        return redirect("login")



def createBills(request):
    if request.user.is_authenticated:

        if request.method == "POST":

            if request.POST['bill_amount'] and request.POST['form_date'] and request.POST['to_date'] and request.POST['payment_date'] and request.FILES['receipt_image'] is not None:
                created_by = request.user.id
                landowner_id = request.POST['landowner_id']
                bill_category_id = request.POST['bill_category_id']
                bill_category_name = request.POST['bill_category_name']
                bill_amount = request.POST['bill_amount']
                form_date = request.POST['form_date']
                to_date = request.POST['to_date']
                payment_date = request.POST['payment_date']
                receipt_image = request.FILES['receipt_image']
                note = request.POST['note']
                form = datetime.fromisoformat(form_date).timestamp()
                to = datetime.fromisoformat(to_date).timestamp()
                payment = datetime.fromisoformat(payment_date).timestamp()

                bill_save = Bill_table(created_by=created_by,landowner_id=landowner_id,bill_category_id=bill_category_id,bill_category_name=bill_category_name,bill_amount=bill_amount,form_date=form,to_date=to,payment_date=payment,receipt_image=receipt_image,note=note)
                bill_save.save()

                #timestamp = datetime.fromisoformat(form_date).timestamp()
                #dt = datetime(2015, 10, 19)
                #timestamp = dt.timestamp()
            
                return redirect(bills)
            
            else:
                owner = Owner.objects.filter(user_id=request.user.id)
                bill_category = Bill_Categories.objects.filter(user_id=request.user.id)
                return render(request,'create_bills.html',{'title':'Create Bills','owner':owner,'bill_category':bill_category})
        
        else:
            owner = Owner.objects.filter(user_id=request.user.id)
            bill_category = Bill_Categories.objects.filter(user_id=request.user.id)
            return render(request,'create_bills.html',{'title':'Create Bills','owner':owner,'bill_category':bill_category})

    else:
        return redirect("login")
    


def editBills(request,nid): 
    if request.user.is_authenticated:

        owner = Owner.objects.filter(user_id=request.user.id)
        bills = Bill_Categories.objects.filter(user_id=request.user.id)
        instance= get_object_or_404(Bill_table,id=nid)
        form= Bill_tableForm(request.POST or None, instance=instance)
        
 
        if form .is_valid():
            print("ewiuohio")
            instance= form.save(commit=False)
            instance.save()
            return redirect("bills")
        print("not work")
        contex={
        'form':form,
        'instance':instance,
        'title':'Update Bills',
        'owner':owner,
        'bills': bills,
        }
        return render(request,'update_bills.html',contex)
    else:
        return redirect("login")




def deleteBills(request,nid):
    if request.user.is_authenticated:
        instance= get_object_or_404(Bill_table,id=nid)
        instance.delete()
        return redirect("bills")

    else:
        return redirect("login")
