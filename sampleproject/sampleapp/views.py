from django.shortcuts import render,HttpResponse,redirect
from .forms import writer,Author,CollegeForm ,SchoolForm, HospitalForm, CollectionForm,ShopForm
from .models import Books, Employee, EmployeePoints, Library, Hospital, Collection,Book,Shop, Person, Trainer, testing_img
from django.template import loader

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
    
# ==========================================================================================

# CRED OPERATIONS on model forms

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

# ==========================================================================================

# CRUD operations 

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

# ==========================================================================================

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

# ==========================================================================================

def shop_create(request):
    if request.method == "POST":
        z=ShopForm(request.POST)
        if z.is_valid():
            z.save()
            return HttpResponse("Shop data added successfully")
    else:
        x=ShopForm()
        return render(request,"shop.html",{"view":x})
    
# ==========================================================================================

    
def person(request):
    if request.method=='POST':
        name=request.POST['name']
        gender=request.POST['gender']
        p=Person.objects.create(name=name,gender=gender)
        p.save()
        return redirect(person_view)
    else:
        return render(request,"person.html")
    
def person_view(request):
    persons = Person.objects.all()  # Fetch all Person objects from the database
    return render(request, "person_view.html", {"persons": persons})  # Pass the Person objects to the template

def person_delete(request, id):
    person = Person.objects.get(id=id)  # Get the Person object by its ID
    person.delete()  # Delete the Person object
    return redirect(person_view)  # Redirect to the person view page after deletion

def person_edit(request, id):
    person = Person.objects.get(id=id)  # Get the Person object by its ID
    return render(request, "person_edit.html", {"person": person})

def person_update(request, id):
    if request.method == "POST":
        name = request.POST['name']
        gender = request.POST['gender']
        person = Person.objects.get(id=id)
        person.name = name
        person.gender = gender
        person.save()
        return redirect(person_view)

# ==========================================================================================

def imagefiles(request):
    if request.method == "POST":
        title = request.POST['title']
        image = request.FILES['image']
        img = testing_img.objects.create(title=title, images=image)
        img.save()
        return redirect(imagefiles_view)
    else:
        return render(request, "imagefiles.html")
    
def imagefiles_view(request):
    images = testing_img.objects.all()  # Fetch all testing_img objects from the database
    return render(request, "imagefiles_view.html", {"images": images})  # Pass the testing_img objects to the template

def imagefiles_delete(request, id):
    image = testing_img.objects.get(id=id)  # Get the testing_img object by its ID
    image.delete()  # Delete the testing_img object
    return HttpResponse("<script>alert('Deleted successfully');window.location.href='http://127.0.0.1:8000/imagefiles_view';</script>")

def imagefiles_edit(request, id):
    image = testing_img.objects.get(id=id)  # Get the testing_img object by its ID
    return render(request, "imagefiles_edit.html", {"image": image})  # Render the edit form with the testing_img object data

# def imagefiles_update(request, id):
#     if request.method == "POST":
#         title = request.POST['title']
#         image = request.FILES['image']
#         img = testing_img.objects.get(id=id)  # Get the testing_img object by its ID
#         img.title = title
#         img.images = image
#         img.save()
#         return HttpResponse("<script>alert('Updated successfully');window.location.href='http://127.0.0.1:8000/imagefiles_view';</script>")

# in above code,it only updates the image not name , below code updates both image and name

def imagefiles_update(request, id):
    if request.method == "POST":
        
        title = request.POST['title']
        img = testing_img.objects.get(id=id)  # Get the testing_img object by its ID
        if 'image' in request.FILES:
            image = request.FILES['image']
            img.images = image
        
        img.title = title
        
        img.save()
        return redirect(imagefiles_view)
    
# ==========================================================================================

# cookie set and get
def setcookie(request):
    r=HttpResponse("Cookie Set")
    r.set_cookie("django","django is a web framework")
    return r

def getcookie(request):
    r=request.COOKIES['django']
    return HttpResponse(r)

def setsession(request):
    request.session['email']="abc@gmail.com"
    return HttpResponse("Session Set")

def getsession(request):
    r=request.session['email']
    return HttpResponse(r)

def deletesession(request):
    del request.session['email']  # Delete the session variable
    return HttpResponse("Session deleted successfully")
    

# ==================================================================== 

def Home(request):
    return render(request,"Homepage.html")   

def Login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        request.session['username'] = username  # Store the username in the session
        return redirect(UserEdit)
    else:    
        return render(request,"userlogin.html")
    
def UserEdit(request):
    username=request.session['username']  # Get the username from the session
    return render(request,"UserEdit.html",{"username":username})

def userLogout(request):
    del request.session['username']  # Delete the username from the session
    return redirect(Home)  # Redirect to the home page after logout


# ==================================================================== 
# GENERIC VIEWS for CRUD operations-class based crud operations
# 

from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView # Importing generic views

class Trainercreate(CreateView):
    model=Trainer
    fields=['name','age','place','email','phone']
    template_name="trainer_create.html"
    success_url="/listview/"  # Redirect to the view page after creating a new trainer

class TrainerList(ListView):
    model=Trainer
    template_name="trainer_list.html"
    context_object_name="trainers"  # Name of the context variable to be used in the template

class Trainerdetail(DetailView):    
    model=Trainer
    template_name="trainer_detail.html"
    context_object_name="trainer"  # Name of the context variable to be used in the template

class Trainerdelete(DeleteView):
    model=Trainer
    template_name="trainer_delete.html"
    success_url="/listview/"  # Redirect to the view page after deleting a trainer

class Trainerupdate(UpdateView):
    model=Trainer
    fields=['name','age','place','email','phone']
    template_name="trainer_create.html"
    success_url="/listview/"  # Redirect to the view page after updating a trainer    

# ==================================================================== 
 

#  GENERIC VIEWS for CRUD operations-function based crud operations
# 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from django.urls import reverse_lazy 

def books_create(request):
    view=CreateView.as_view(
        model=Books,
        template_name='books_create.html',
        fields=['title', 'author', 'published_date','isbn'],
        success_url=reverse_lazy('books_list')  # Redirect to the book list view after creating a new book
    )
    return view(request) # Call the view function with the request object

def books_list(request):
    view=ListView.as_view(
        model=Books,
        template_name='books_list.html',
        context_object_name='books'
    )
    return view(request)

def books_detail(request, pk):
    view=DetailView.as_view(
        model=Books,
        template_name='books_detail.html',
        context_object_name='book'
    )
    return view(request, pk=pk)  # Pass the primary

def books_update(request, pk):
    view=UpdateView.as_view(
        model=Books,
        template_name='books_create.html',
        fields=['title', 'author', 'published_date','isbn'],
        success_url=reverse_lazy('books_list')  # Redirect to the book list view after updating a book
    )
    return view(request, pk=pk)  # Pass the primary key of the book to be updated

def books_delete(request, pk):
    view=DeleteView.as_view(
        model=Books,
        template_name='books_delete.html',
        success_url=reverse_lazy('books_list')  # Redirect to the book list view after deleting a book
    )
    return view(request, pk=pk)  # Pass the primary


# createview is a generic class based view-->for creating objects
# as_view() converts class based view into function based view
# then can be called with a request to produce a response
# reverse_lazy ==dynamically generates the url for the view named 'books_list'

# ====================================================================


#send email

from django.core.mail import send_mail
from sampleproject import settings

def new_email(request):
    subject = "Test Email"
    message = "This is a test email sent from Django."
    to="itzmenavz@gmail.com"

    r=send_mail(subject, message, settings.EMAIL_HOST_USER, [to])
    if r:
        return HttpResponse("Email sent successfully")
    else:
        return HttpResponse("Failed to send email")

# ====================================================================

def EmployeeCreate(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        age = request.POST['age']
        email = request.POST['email']
        phone = request.POST['phone']
        
        employee = Employee.objects.create(
            first_name=first_name,
            last_name=last_name,
            age=age,
            email=email,
            phone=phone
        )
        employee.save()
        return redirect(EmployeeList)
    else:
        return render(request, "employee_create.html")
    

def EmployeeList(request):
    employees = Employee.objects.all()  # Fetch all Employee objects from the database
    return render(request, "employee_list.html", {"employees": employees})  # Pass the Employee objects to the template 

def EmployeeDelete(request, id):
    employee = Employee.objects.get(id=id)  # Get the Employee object by its ID
    employee.delete()  # Delete the Employee object
    return redirect(EmployeeList)  # Redirect to the employee list page after deletion

def EmployeeUpdate(request, id):
    employee = Employee.objects.get(id=id)  # Get the Employee object by its ID
    if request.method == "POST":
        employee.first_name = request.POST['first_name']
        employee.last_name = request.POST['last_name']
        employee.age = request.POST['age']
        employee.email = request.POST['email']
        employee.phone = request.POST['phone']
        employee.save()
        return redirect(EmployeeList)  # Redirect to the employee list page after updating
    return render(request, "employee_update.html", {"employee": employee})  # Render the update form with the Employee object data

def EmployeePointCreate(request):
    if request.method == "POST":
        employee_id = request.POST['employee_id']  # Get the Employee ID from the form data
        points = request.POST['points']
        employee = Employee.objects.get(id=employee_id)  # Get the Employee object by its ID
        employee_point = EmployeePoints.objects.create(employee=employee, points=points)
        employee_point.save()
        return redirect(EmployeePointList)  # Redirect to the employee list page after creating a new point
    else:
        employee_id = Employee.objects.all()
        return render(request, "employee_point_create.html", {"employee_id": employee_id})  # Render the point creation form with the Employee ID
    
def EmployeePointList(request):
    employee_points = EmployeePoints.objects.all()  # Fetch all EmployeePoints objects from the database
    return render(request, "employee_point_list.html", {"employee_points": employee_points})  # Pass the EmployeePoints objects to the template    

def new_function(request):
    x="django"
    y=loader.get_template('hello.html')    
    return HttpResponse(y.render({"data":x}))  # Render the 'hello.html' template with the context data