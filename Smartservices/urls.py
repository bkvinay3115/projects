"""
Definition of urls for Smartservices.
"""

from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

import app.views
import app.forms

urlpatterns = [
    path('', app.views.home, name='home'),
    path('contact', app.views.contact, name='contact'),
    path('about', app.views.about, name='about'),
    path('view_service', app.views.view_service, name='view_service'),
    path('customer_profile', app.views.customer_profile, name='customer_profile'),
    path('myservicebookings', app.views.myservicebookings,
         name='myservicebookings'),
    path('serviceprov_profile', app.views.serviceprov_profile,
         name='serviceprov_profile'),
    path('addservices', app.views.addservices, name='addservices'),
    path('changepassword', app.views.changepassword, name='changepassword'),
    path('feedback', app.views.feedback, name='feedback'),
    path('bookedservices', app.views.bookedservices, name='bookedservices'),
    path('approvedservices', app.views.approvedservices, name='approvedservices'),
    path('sign_up', app.views.sign_up, name='sign_up'),

    path(
        'editprofile/<int:id>',
        app.views.editprofile,
        name='editprofile'
    ),

    path(
        'bookservice/<int:id>',
        app.views.bookservice,
        name='bookservice'
    ),

    path(
        'payments/<int:id>',
        app.views.payments,
        name='payments'
    ),

    path(
        'serviceapproval/<int:id>',
        app.views.serviceapproval,
        name='serviceapproval'
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='app/login.html',
            authentication_form=app.forms.BootstrapAuthenticationForm
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(
            next_page='/'
        ),
        name='logout'
    ),

    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
