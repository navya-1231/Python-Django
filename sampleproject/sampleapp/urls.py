from django.urls import path
from sampleapp.views import *

urlpatterns = [
    path('first',display),
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
]
