from django.shortcuts import render, HttpResponse,redirect
from firstapp.forms import SiteUserForm,UserNameForm,ImageUserForm
from firstapp.models import SiteUser,UserRole,UserImage
from django.core.files.storage import FileSystemStorage #for image in media
from django.contrib.auth.hashers import make_password,check_password
import os
def index(request):
    return HttpResponse("<h1> welcome to first response<h1>")
def home(request):
    return render(request,"home.html")
def about(request):
    name="NITIN"
    names=["nitin","name2","name3"]
    return render(request,"about.html",{'n':name,'l':names})
def testhome(request):
    return render(request,"cont.html")
def testhome2(request):
    return render(request,"testhome.html")
def signup(request):
    if request.method=='POST':
        form=SiteUserForm(request.POST)
        f=form.save(commit=False)
        f.UserFullName=request.POST["fullname"]
        f.UserMobile=request.POST["mobile"]
        f.UserEmail=request.POST["email"]
        f.UserPassword=make_password(request.POST["password"])
        f.isActive=True
        f.roleId_id=1
        f.save()
        return render(request,"signup.html",{'success':True})
    return render (request,"signup.html")
def name(request):
    if request.method=='POST':
        form=UserNameForm(request.POST)
        f=form.save(commit=False)
        f.roleName=request.POST["name"]
        f.IsActive=True
        f.save()
        return render(request,"username.html",{'success':True})
    return render(request,"username.html")

def datafetch(request):
    #data=SiteUser.objects.get(UserEmail="kolishnitin@gmail.com")
    data = SiteUser.objects.all()
    return render(request,"viewdata.html",{'d':data})
    #data=SiteUser.objects.filter(isActive=1)


def imagedata(request):
    if request.method=='POST':
        form=ImageUserForm(request.POST)
        #img1 = None
        try:
            if request.FILES["image1"]:
                my_file = request.FILES["image1"]
                fs = FileSystemStorage()     #Used to store files or images on database
                file_name = fs.save(my_file.name, my_file)
                img1 = fs.url(file_name)
                img1 = my_file.name
        except:
            pass
        f = form.save(commit=False)
        f.roleId=request.POST["id"]
        f.UserFullName=request.POST["fullname"]
        f.UserMobile=request.POST["mobile"]
        f.UserEmail=request.POST["email"]
        f.UserPassword=request.POST["password"]
        f.isActive=True
        f.UserImage = img1
        f.save()
        return render(request,"Userimage.html",{'success':True})
    return render(request,"Userimage.html")
def UpdateData(request):
    if request.method == 'POST':
        if request.method == 'POST':
            try:
                if request.FILES["image1"]:
                    os=name("media/" + data.)
                    my_file = request.FILES["image1"]
                    fs = FileSystemStorage()  # Used to store files or images on database
                    file_name = fs.save(my_file.name, my_file)
                    img1 = fs.url(file_name)
                    img1 = my_file.name
            except:
                pass
        name1=request.POST["fullname"]
        email1=request.POST["email"]
        password1=request.POST["password"]
        mobile1=request.POST["mobile"]
        image2=img1
        updatedata=UserImage(UserEmail=email1,UserFullName=name1,UserPassword=password1,UserMobile=mobile1,UserImage=image2)
        updatedata.save(update_fields=["UserFullName","UserPassword","UserMobile","UserImage"])
        return render(request,"update.html",{'success':True} )
    return render(request,"update.html")
def deletedata(request):
    id=request.GET["id"]
    data=SiteUser.objects.get(UserEmail=id)
    data.delete()
    return redirect("/viewdata")
def datafetch2(request):
    id2 = request.GET["id"]
    data = SiteUser.objects.get(UserEmail=id2)
    #data=SiteUser.objects.get(UserEmail="kolishnitin@gmail.com")
    #data = SiteUser.objects.all()

    #data=SiteUser.objects.filter(isActive=1)
    if request.method == 'POST':
       name1 = request.POST["fullname"]
       password1 = request.POST["password"]
       mobile1 = request.POST["mobile"]

       updatedata = SiteUser(UserEmail=data.UserEmail, UserFullName=name1, UserPassword=password1, UserMobile=mobile1)
       updatedata.save(update_fields=["UserFullName", "UserPassword", "UserMobile"])
       return render(request, "viewdata.html",{'success':True})
    return render(request,"edit.html",{'d':data})