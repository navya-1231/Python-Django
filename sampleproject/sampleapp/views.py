from django.shortcuts import render,HttpResponse
from .forms import writer,Author,CollegeForm ,SchoolForm, HospitalForm
from .models import Library, Hospital
# Create your views here.

# request:parameter represents the HTTP request sent by the user to the server

def display(request):
    return HttpResponse("welcome to django")
def display1(request):
    return HttpResponse("<h1>welcome to django</h1>")
def display2(request):
    return HttpResponse("<i>welcome to django</i>")


def helloview(request):
    a="django"
    b="python"
    c=[1,2,3,4,5,6,7,8,9,10]
    return render(request,"one.html",{"data":a,"view":b,"list1":c}) 
    
def one(request):
    return render(request,"two.html")

def write(request):
    x=writer
    return render(request,"write.html",{"data":x})

def authors(request):
    if request.method=="POST":
        f=Author(request.POST)
        if f.is_valid():
            name=f.cleaned_data["name"]
            place=f.cleaned_data["place"]   
            age=f.cleaned_data["age"]
            # return render(request,"view.html",{"data":name,"view":place,"value":age})
            return HttpResponse(f"Author Name: {name}, Author Place: {place}, Author Age: {age}")
    else:
        x=Author
        return render(request,"author.html",{"data":x})

def collegeview(request):
    if request.method=="POST":
        z=CollegeForm(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("worked")
    else:
        x=CollegeForm
        return render(request,"college.html",{"view":x})
    
def schoolview(request):
    if request.method=="POST":
        z=SchoolForm(request.POST,request.FILES)
        if z.is_valid():
            z.save()
            return HttpResponse("uploaded successfully")
        return HttpResponse("not working")
    else:
        x=SchoolForm
        return render(request,"school.html",{"view":x})
    
def parent(request):
    return render(request,"parent.html")

def child(request):
    return render(request,"child.html")

def index(request):
    return render(request,"index.html")

def lib(request):
    if request.method == "POST":
        book = request.POST['book']
        author = request.POST['author']
        price = request.POST['price']
        x=Library.objects.create(book_name=book, author_name=author, price=price) # Create a new Library object for the book from the form data
        x.save()
        return HttpResponse("Book added successfully")
    else:
        return render(request,"lib.html")
    
# CRED OPERATIONS 

# CREATE
def hospitalview(request):
    if request.method == "POST":
        z=HospitalForm(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("worked")
    else:
        x=HospitalForm
        return render(request,"hospital.html",{"view":x})

# READ
def viewhospital(request):
    x=Hospital.objects.all()  # Fetch all Hospital objects from the database
    return render(request,"viewhospital.html",{"data":x})  # Pass the Hospital