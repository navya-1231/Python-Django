"""
URL configuration for sampleproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from sampleapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('view',views.display),
    # path('view1',views.display1),
    # path('view2',views.display2)
    path("",include("sampleapp.urls"))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # This will serve media files during development. In production, you should configure your web server to serve these files.

# when you upload an images using an imagefiles in a model
# django will save the file to media root and then construct the url to access this file using media url