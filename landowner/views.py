from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Owner
from .forms import OwnerForm
# Create your views here.

def mainhome(request):
    if request.user.is_authenticated:
        return render(request,'main.html',{'title':'Home'})
    else:
        return redirect("login")


def register(request):

    if request.method == "POST":
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