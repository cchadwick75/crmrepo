from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import *

admin.autodiscover()



urlpatterns = [
    # Action Views (part of the core package)
    path('', login_required(CustomerMain.as_view()), name='customer'),

]