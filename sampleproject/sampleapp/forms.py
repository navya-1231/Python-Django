from django import forms
from .models import College, School, Hospital, Collection,Shop, Person

class writer(forms.Form):
    name=forms.CharField(max_length=30)
    place=forms.CharField(max_length=30)
    age=forms.IntegerField()
 
class Author(forms.Form):
    name=forms.CharField(max_length=30,label="Author Name")
    place=forms.CharField(max_length=30,label="Author Place")
    age=forms.IntegerField(label="Author Age")

class CollegeForm(forms.ModelForm):
    class Meta: #class meta is used to define metadata for the form
        # This class is used to create a form based on the College model
        model = College
        fields = "__all__"  # This will include all fields from the College model

class SchoolForm(forms.ModelForm):
    class Meta:
        model = School
        fields = "__all__"  # This will include all fields from the School model

class HospitalForm(forms.ModelForm): # Hospital form to handle Hospital model data
    class Meta:
        model = Hospital #  Hospital model data 
        fields = "__all__"  # This will include all fields from the Hospital model
        # fields = ['name', 'age']  # Specify the fields to include in the form
        # exclude = ['place']  # Exclude the 'place' field from the form

class CollectionForm(forms.ModelForm):
    class Meta: # Collection form to handle Collection model data
        model = Collection # model name
        fields = "__all__"  # This will include all fields from the Collection model

# class ShopForm(forms.ModelForm):
#     class Meta:
#         model = Shop
#         fields = ['firstname', 'lastname', 'place']  # Specify the fields to include in the form

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        exclude = ['email']  # Exclude the 'email' field from the form

 