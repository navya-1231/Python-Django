from django.shortcuts import render,HttpResponse,redirect
from .forms import writer,Author,CollegeForm ,SchoolForm, HospitalForm, CollectionForm,ShopForm
from .models import Library, Hospital, Collection,Book,Shop
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

# CREATE ,add new hospital data
def hospitalview(request):
    if request.method == "POST":
        z=HospitalForm(request.POST)
        if z.is_valid():
            z.save()
            # return HttpResponse("worked")
            return redirect(viewhospital)
    else:
        x=HospitalForm
        return render(request,"hospital.html",{"view":x})

# READ
def viewhospital(request):
    x=Hospital.objects.all()  # Fetch all Hospital objects from the database
    return render(request,"viewhospital.html",{"data":x})  # Pass the Hospital

# DELETE

def delete_hospital(request, id):
    x=Hospital.objects.get(id=id)  # Get the Hospital object by its ID
    print(x)  # Print the Hospital object to the console (for debugging)
    x.delete()  # Delete the Hospital object
    # return HttpResponse("Deleted successfully")  # Return a success message
    # return redirect(viewhospital)  # Redirect to the view hospital page after deletion
    return HttpResponse("<script>alert('Deleted successfully');window.location.href='http://127.0.0.1:8000/view';</script>")  # Use JavaScript to show an alert and redirect to the view hospital page

# EDIT & UPDATE

def edit_hospital(request, id):
    x=Hospital.objects.get(id=id)  # Get the Hospital object by its ID
    return render(request,"edithospital.html",{"data":x})  # Render the edit form with the Hospital object data

def update_hospital(request, id):
    if request.method == "POST":
        x=Hospital.objects.get(id=id)  # Get the Hospital object by its ID
        # Update the Hospital object with the data from the form
        z=HospitalForm(request.POST,instance=x)  # Create a form instance with the POST data and the existing Hospital object 
        if z.is_valid():
            z.save()
            # return HttpResponse("updated successfully")
            return redirect(viewhospital)
        return HttpResponse("not working")
    return HttpResponse("Invalid request method")  # Handle invalid request methods

# CRUD operations for the Collection model
def collection_view(request):
    if request.method=='POST':
        coll_form=CollectionForm(request.POST,request.FILES)  # Create a form instance with the POST data and uploaded files
        # request.FILES is used to handle file uploads in Django forms
        if coll_form.is_valid():
            coll_form.save()
            # return HttpResponse("Document Added successfully")
            return redirect(view_collection)
        return HttpResponse("not working")    
    else:
        collection_form = CollectionForm
        return render(request,"collection.html",{"form":collection_form})
    
def view_collection(request):
    collections = Collection.objects.all()  # Fetch all Collection objects from the database
    return render(request,"viewcollection.html",{"data":collections})  # Pass the Collection objects to the template    

def delete_collection(request, id):
    collection = Collection.objects.get(id=id)  # Get the Collection object by its ID
    collection.delete()  # Delete the Collection object
    return HttpResponse("<script>alert('Deleted successfully');window.location.href='http://127.0.0.1:8000/c_view';</script>")  # Use JavaScript to show an alert and redirect to the view hospital page

def edit_collection(request, id):
    collection = Collection.objects.get(id=id)  # Get the Collection object by its ID
    return render(request,"editcollection.html",{"data":collection})  # Render the edit form with the Collection object data

def update_collection(request, id):
    collection = Collection.objects.get(id=id)  # Get the Collection object by its ID
    if request.method == "POST":
          # Get the Collection object by its ID
        coll_form = CollectionForm(request.POST, request.FILES, instance=collection)  # Create a form instance with the POST data and existing Collection object
        if coll_form.is_valid():
            coll_form.save()
            return redirect(view_collection)  # Redirect to the view collection page after updating
        return render(request, "editcollection.html", {"data": collection})  # Render the edit form again if the form is not valid

# CRUD operations for the normal forms

def book_create(request):
    if request.method=='POST':
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        price = request.POST['price']
        book = Book.objects.create(book_name=book_name, author_name=author_name, price=price)
        book.save()
        return redirect(book_view)  # Redirect to the book view page after creating a new book
    else:
        return render(request, "book_create.html")
    
def book_view(request):
    books = Book.objects.all()  # Fetch all Book objects from the database
    return render(request, "book_view.html", {"books": books})

def book_delete(request, id):
    book = Book.objects.get(id=id)  # Get the Book object by its ID
    book.delete()  # Delete the Book object
    return HttpResponse("<script>alert('Deleted successfully');window.location.href='http://127.0.0.1:8000/bview';</script>")

def book_edit(request, id):
    book = Book.objects.get(id=id)  # Get the Book object by its ID
    return render(request, "book_edit.html", {"book": book})  # Render the edit form with the Book object data

def book_update(request, id):
    if request.method == "POST":
        book_name = request.POST['book_name']
        author_name = request.POST['author_name']
        price = request.POST['price']
        book = Book.objects.get(id=id)
        book.book_name = book_name
        book.author_name = author_name  
        book.price = price
        book.save()
        return HttpResponse("<script>alert('Updated successfully');window.location.href='http://127.0.0.1:8000/bview';</script>")  # Redirect to the book view page after updating

def shop_create(request):
    if request.method == "POST":
        z=ShopForm(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("Shop data added successfully")
    else:
        x=ShopForm()
        return render(request,"shop.html",{"view":x})
    
