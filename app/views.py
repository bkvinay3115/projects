"""
Definition of views.
"""

from django.shortcuts import render,redirect
from django.http import HttpRequest,HttpResponse
from django.template import RequestContext
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from app.forms import SignUpForm,ServiceProviderForm,ServiceBookingForm,ServiceApproveForm,PaymentForm
from app.models import Profile,serviceprovider,Servicebooking,Payment
from django.db.models import Q
from django.core.mail import send_mail
from Smartservices.settings import EMAIL_HOST_USER
from twilio.rest import Client

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'',
            'year':datetime.now().year,
        }
    )

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            flag=False
            uname=form.cleaned_data.get('username')
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            
            if request.POST.get("type")=="Customer":
                user.profile.is_customer=True
            else:
                user.profile.is_serviceprovider=True
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
            #flag=True
            #return render(request, 'sign_up.html', {'form': form,"notfound":flag })
    else:
        form = SignUpForm()
    return render(request, 'app/sign_up.html', {'form': form})

def view_service(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    services=serviceprovider.objects.all().order_by('-created_date')
    if request.method=="GET":
        return render(
        request,
        'app/view_service.html',
        {
            'services':services,
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def customer_profile(request):
    assert isinstance(request, HttpRequest)
    cust_profile=User.objects.get(username=request.user)
    if request.method=="GET":
        return render(
        request,
        'app/customer_profile.html',
        {
            'cust_profile':cust_profile,
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def serviceprov_profile(request):
    assert isinstance(request, HttpRequest)
    sp_profile=User.objects.get(username=request.user)
    return render(
        request,
        'app/serviceprov_profile.html',
        {
            'sp_profile':sp_profile,
            'title':'Profile Service Provider',
            'message':'Profile',
            'year':datetime.now().year,
        }
    )

def editprofile(request,id):
    prof=User.objects.get(pk=id)
    success=False
    if request.method=="GET":
        return render(request,'app/editprofile.html',{"u_profile":prof})
    elif request.method=="POST":
        prof.first_name=request.POST.get("first_name")
        prof.last_name=request.POST.get("last_name")
        prof.email=request.POST.get("email")
        prof.profile.contact=request.POST.get("contact")
        prof.save()
        success=True
        return redirect('/customer_profile')
 
   
def addservices(request):
    assert isinstance(request, HttpRequest)
    sp_profile=User.objects.all().filter(username=request.user)[0]
    success=False
    if request.method=="GET":
        form=ServiceProviderForm(request.GET)
        return render(
        request,
        'app/addservices.html',
        {
            'form':form,
            'sp_profile':sp_profile,
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        })
    elif request.method=="POST":
        form=ServiceProviderForm(request.POST,request.FILES)
        if form.is_valid():
            service=form.save()
            service.refresh_from_db()
            service.save()
            success=True
            return render(request,'app/addservices.html',{"success":success})
    return  render(request,'app/addservices.html')
 

def bookservice(request,id):
    service=serviceprovider.objects.get(pk=id)
    customer=User.objects.all().filter(username=request.user)[0]
    if request.user.is_authenticated(): 
        success=False
        if request.method=="GET":    
            form=ServiceBookingForm()
            return render(request,'app/bookservice.html',{ 'form':form,    
            'service':service,
            'customer':customer,
            'message':'Your contact page.',
            'year':datetime.now().year,
         })
        elif request.method=="POST":
            form=ServiceBookingForm(request.POST)
            if form.is_valid():
                booking=form.save()
                booking.refresh_from_db()
                booking.save()
                success=True
                ser_email=service.email
                emailid=customer.email
               # send_mail('Service Booked','Dear customer your Service Booked Successfully and wait for approval.', EMAIL_HOST_USER, [emailid], fail_silently = False)
               # send_mail('Service Booked With you','Dear service provider provide best service to the customer and wait for approval.', EMAIL_HOST_USER, [ser_email], fail_silently = False)
                #watsapp()
                return render(request,'app/bookservice.html',{"success":success})
    return redirect('/view_service')

def myservicebookings(request):
    if request.user.is_authenticated():
         bookings=Servicebooking.objects.all().filter(username=request.user)
         customer_profile=User.objects.all().filter(username=request.user)[0]
         return render(
        request,
        'app/myservicebookings.html',
        {
            'bookings':bookings,
            'cust_profile':customer_profile,
            'title':'My service bookings',
            #'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )
def changepassword(request):
    u_profile=User.objects.get(username=request.user)
    success=False
    if request.method=="GET":
        form=PasswordChangeForm(request.user)
        return render(request,'app/changepassword.html',{"form":form,"u_profile":u_profile})
    elif request.method=="POST":
         form = PasswordChangeForm(request.user, request.POST)
         if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
           # messages.success(request, 'Your password was successfully updated!')
            success=True      
            return render(request,'app/changepassword.html',{"success":success})
        
def feedback(request):   
    if request.method=="GET":
        bookings=Servicebooking.objects.all().filter(username=request.user)
        return render(request,'app/feedback.html',{"bookings":bookings})
    if request.method=="POST":
        bid=request.POST.get("b_id")
        feed_back=request.POST.get("feed_back")
        booking=Servicebooking.objects.all().filter(id=bid)[0]
        booking.feedback=feed_back
        booking.save()
        booking.refresh_from_db()
        return redirect('/feedback')

def payments(request,id):
    if request.method=="GET":
        booking=Servicebooking.objects.get(id=id)       
        return render(request,'app/paymentdetails.html',{'booking':booking})
    elif request.method=="POST":
        booking=Servicebooking.objects.get(id=id)
        totAmt=request.POST.get("tot_amt")
        booking.payment.paidamount=int(totAmt)
        booking.payment.save()
        return redirect('/myservicebookings')

def bookedservices(request):
    #queryset=Servicebooking.objects.all().filter(sbapproval='Not Approved')|Servicebooking.objects.all().filter(sbapproval='Pending')
    bookings=Servicebooking.objects.all().filter(Q(sbapproval='Not Approved')|Q(sbapproval='Pending')).order_by('-bookingdate')
    #bookings=Servicebooking.objects.all().filter(sbapproval='Not Approved').order_by('-bookingdate')
    if request.method=='GET':
       # sbook=Servicebooking.objects.get(id=id)
        #form=ServiceApproveForm(instance=sbook)
        return render(request,'app/bookedservices.html',{"bookings":bookings})

def serviceapproval(request,id):
    bookings=Servicebooking.objects.all().order_by('-bookingdate')
    if request.method=='GET':
        sbook=Servicebooking.objects.get(id=id)
        spayment=Payment.objects.get(sbid=id)
        form1=ServiceApproveForm(instance=sbook)
        form2=PaymentForm(instance=spayment)
        return render(request,'app/serviceapprovalform.html',{"bookings":bookings,"form1":form1,"form2":form2})
    elif request.method=='POST':
        sbook=Servicebooking.objects.get(id=id)
        spayment=Payment.objects.get(sbid=id)
        form1=ServiceApproveForm(request.POST,instance=sbook)
        form2=PaymentForm(request.POST,instance=spayment)
        if form1.is_valid():
           sbook=form1.save()
           sbook.save()
        if form2.is_valid():
            spayment=form2.save()
            spayment.save()
        return redirect('/bookedservices')

def approvedservices(request):
    #queryset=Servicebooking.objects.all().filter(sbapproval='Not Approved')|Servicebooking.objects.all().filter(sbapproval='Pending')
    bookings=Servicebooking.objects.all().filter(Q(sbapproval='Approved')|Q(sbapproval='Pending')).order_by('-bookingdate')
    #bookings=Servicebooking.objects.all().filter(sbapproval='Not Approved').order_by('-bookingdate')
    if request.method=='GET':
       # sbook=Servicebooking.objects.get(id=id)
        #form=ServiceApproveForm(instance=sbook)
        return render(request,'app/approvedservices.html',{"bookings":bookings})

def watsapp():
  # Your Account Sid and Auth Token from twilio.com/console
  # DANGER! This is insecure. See http://twil.io/secure
    account_sid = 'ACdd326facf0e3a20901679b0b3d4e6608'
    auth_token = '963560e8c5c302f67d96110f4f3355c7'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                              from_='whatsapp:+917022955501',
                              body='Hello,prasahant your service Booked withus',
                              to='whatsapp:+919916491921'
                          )

