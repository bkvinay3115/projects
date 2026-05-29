"""
Definition of urls for Smartservices.
"""

from datetime import datetime
from django.conf.urls import url
from django.conf.urls.static import static
import django.contrib.auth.views
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),
    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^view_service$', app.views.view_service , name='view_service'),
    url(r'^customer_profile$', app.views.customer_profile , name='customer_profile'),
    url(r'^myservicebookings$', app.views.myservicebookings, name='myservicebookings'),
    url(r'^serviceprov_profile$', app.views.serviceprov_profile, name='serviceprov_profile'),
    url(r'^editprofile/(?P<id>\d+)$', app.views.editprofile, name='editprofile'),
    url(r'^addservices$', app.views.addservices, name='addservices'),
    #url(r'^bookservice$', app.views.bookservice, name='bookservice'),
    url(r'^bookservice/(?P<id>\d+)$', app.views.bookservice, name='bookservice'),
    url(r'^changepassword$', app.views.changepassword, name='changepassword'),
    url(r'^payments/(?P<id>\d+)$', app.views.payments, name='payments'),
    url(r'^feedback$', app.views.feedback, name='feedback'),
    url(r'^bookedservices$', app.views.bookedservices, name='bookedservices'),
    url(r'^approvedservices$', app.views.approvedservices, name='approvedservices'),
    url(r'^serviceapproval/(?P<id>\d+)$', app.views.serviceapproval, name='serviceapproval'),
    url(r'^login/$',
        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Log in',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    url(r'^sign_up$', app.views.sign_up, name='sign_up'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)