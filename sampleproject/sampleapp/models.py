from django.db import models

# Create your models here.

# pip install virtualenv

# python -m virtualenv venv

# cmd

# venv\Scripts\activate

# pip install django

# django-admin startproject projectname

# cd projectname

# py manage.py startapp appname

# py manage.py runserver

# django is mvt model-view-template architecture

class Student(models.Model):
    name=models.CharField(max_length=20)
    rollno=models.IntegerField()
    marks=models.FloatField()
    
class Teacher(models.Model):
    name=models.CharField(max_length=20)
    place=models.CharField(max_length=20)
    age=models.IntegerField()
    class Meta:
        db_table='Teacher'

class College(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()

class School(models.Model):
    name=models.CharField(max_length=30)
    doc=models.FileField(upload_to='media')

class Library(models.Model):
    book_name=models.CharField(max_length=30)
    author_name=models.CharField(max_length=50)
    price=models.IntegerField()

class Hospital(models.Model):
    name=models.CharField(max_length=30)
    place=models.CharField(max_length=30)
    age=models.IntegerField()

class Collection(models.Model):
    name=models.CharField(max_length=30)
    document=models.FileField(upload_to='media')

class Book(models.Model):
    book_name=models.CharField(max_length=30)
    author_name=models.CharField(max_length=50)
    price=models.IntegerField()
    
class Shop(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    email=models.EmailField(max_length=50)
    place=models.CharField(max_length=30)
   
    