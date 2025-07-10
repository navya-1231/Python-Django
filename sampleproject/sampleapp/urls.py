from django.urls import path
from sampleapp.views import *

urlpatterns = [
    # path('first',display),
    path('hello',helloview),
    path('one',one),
    path('w',write),
    path('a',authors),
    path('c',collegeview),  # Added collegeview URL pattern
    path('s',schoolview),  # Added schoolview URL pattern
    path('p', parent),  # Added parent URL pattern
    path('ch',child),
    path('index', index),  # Added index URL pattern
    path('lib', lib),  # Added library URL pattern

    path('hospital', hospitalview),  # Added hospital form URL pattern
    path('view', viewhospital),  # Added view hospital URL pattern
    path('del_hospital/<int:id>', delete_hospital),  # Added delete hospital URL pattern
    path('edit_hospital/<int:id>', edit_hospital),  # Added edit hospital URL pattern
    path('update_hospital/<int:id>', update_hospital),  # Added update hospital URL pattern
    
    path('collection', collection_view),  # Added collection form URL pattern
    path('c_view', view_collection),  # Added view collection URL pattern
    path('del_collection/<int:id>', delete_collection),  # Added delete collection URL pattern
    path('edit_collection/<int:id>', edit_collection),  # Added edit collection URL pattern
    path('update_collection/<int:id>', update_collection),  # Added update collection URL pattern
    
    path('book', book_create),  # Added book create URL pattern
    path('bview', book_view),  # Added book view URL pattern
    path('dbook/<int:id>', book_delete),  # Added book delete URL pattern
    path('ebook/<int:id>', book_edit),  # Added book edit URL pattern
    path('ubook/<int:id>', book_update),  # Added book update URL pattern


    path('shop', shop_create), 


    path('person', person), 
    path('person_view', person_view),  # Added person view URL pattern
    path('person_delete/<int:id>', person_delete),  # Added person delete URL pattern
    path('person_edit/<int:id>', person_edit),  # Added person edit URL pattern
    path('person_update/<int:id>', person_update),  # Added person update URL pattern


    path('imagefiles', imagefiles),  # Added image files URL pattern
    path('imagefiles_view', imagefiles_view),  # Added image files view URL pattern
    path('imagefiles_delete/<int:id>', imagefiles_delete),  # Added image files delete URL pattern
    path('imagefiles_edit/<int:id>', imagefiles_edit),  # Added image files edit URL pattern
    path('imagefiles_update/<int:id>', imagefiles_update),  # Added image files

    path('setcookie', setcookie),  # Added set cookie URL pattern
    path('getcookie', getcookie),  # Added get cookie URL pattern

    path('setsession', setsession),  # Added set session URL pattern
    path('getsession', getsession),  # Added get session URL pattern
    path('deletesession', deletesession),  # Added delete session URL pattern
    

    path('home', Home),  # Added home URL pattern
    path('Login', Login),  # Added user login URL pattern
    path('UserEdit', UserEdit),  # Added user edit URL pattern
    path('userLogout', userLogout),  # Added user logout URL pattern


    path('trainee/', Trainercreate.as_view(),name='trainer_create'),  # Added trainer create URL pattern
    path('listview/', TrainerList.as_view(), name='trainer_list'),  # Added trainer list view URL pattern
    path('trainer_view/<int:pk>/', Trainerdetail.as_view(), name='trainer_detail'),  # Added trainer view URL pattern 
    path('trainer_update/<int:pk>/', Trainerupdate.as_view(), name='trainer_update'),  # Added trainer update URL pattern
    path('trainer_delete/<int:pk>/', Trainerdelete.as_view(), name='trainer_delete'),  # Added trainer delete URL pattern

    path('books/', books_create, name='books_create'),  # Added books create URL pattern
    path('books_list/', books_list, name='books_list'),  # Added books list view URL pattern
    path('books_detail/<int:pk>/', books_detail, name='books_detail'),  # Added books detail view URL pattern
    path('books_update/<int:pk>/', books_update, name='books_update'),  # Added books update URL pattern
    path('books_delete/<int:pk>/', books_delete, name='books_delete'),

    path('send',new_email),

    path('Employee', EmployeeCreate),  # Added employee create URL pattern
    path('Employee_list', EmployeeList),  # Added employee list view URL pattern
    path('Employee_update/<int:id>', EmployeeUpdate),  # Added employee update URL pattern
    path('Employee_delete/<int:id>', EmployeeDelete),  # Added employee delete URL pattern

    path('point', EmployeePointCreate),  # Added employee point create URL pattern
    path('point_list', EmployeePointList),  # Added employee point list view URL pattern
]