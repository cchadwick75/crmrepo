from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
import django.contrib.auth.views as auth_views
from .views import *

admin.autodiscover()

urlpatterns = [
    # Action Views (part of the core package)
    path('administration', GenericLoginPage.as_view(), name='login' )

]