from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from .models import Owner
from .forms import OwnerForm
# Create your views here.

def mainhome(request):
    if request.user.is_authenticated:
        return render(request,'main.html')
    else:
        return render(request,'home.html')


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
            return render(request,'main.html')

        else:
            messages.info(request,'user name or password wrong')
            return render(request,'login.html')
        

    else:
        return render(request,'login.html')
        


def logout(request):
    auth.logout(request)
    return render(request,'home.html')



def createland(request,nid):

    if request.user.is_authenticated:
        if request.method == "POST":

            name = request.POST['name']
            email = request.POST['email']
            contact = request.POST['contact']
            address = request.POST['address']
            user_id = nid
            user = Owner(name=name,email=email,contact=contact,address=address,user_id=user_id)
            user.save()
            owner = Owner.objects.filter(user_id=nid)
            contex ={
                'nid': nid,
                'owner': owner,
            }

            return redirect("showland",nid)

    
        else:
            return render(request,'createland.html')

    else:
        return render(request,'main.html')


    


def showland(request,usid):
    if request.user.is_authenticated:
        owner = Owner.objects.filter(user_id=usid)
    
        contex={
            
            'owner': owner,
        }
        return render(request,'showland.html',contex)

    else:
        return render(request,'main.html')
    



def delete(request,nid,usid):
    if request.user.is_authenticated:
        instance= get_object_or_404(Owner,id=nid)
        instance.delete()

        '''owner = Owner.objects.filter(user_id=usid)
        print(owner)
        contex = {
            'nid': nid,
            'owner': owner,
        }
        return render(request,'reshow.html',contex)'''

        return redirect("showland",usid)

    else:
        return render(request,'login.html')




def edit(request,nid,usid): 
    if request.user.is_authenticated:

        instance= get_object_or_404(Owner,id=nid)
        form= OwnerForm(request.POST or None, instance=instance)
        
        if form .is_valid():
            instance= form.save(commit=False)
            instance.save()
            return redirect('showland',usid)
    
        contex={
        'form':form,
        'instance':instance,
        }
        return render(request,'update.html',contex)
    else:
        return render(request,'login.html')