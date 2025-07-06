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
] 
