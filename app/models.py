"""
Definition of models.
"""

from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import date


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12, blank=True)
    is_serviceprovider = models.BooleanField(default=False, blank=True)
    is_customer = models.BooleanField(default=False, blank=True)
    is_admin = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return str(self.user)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()


class serviceprovider(models.Model):
    GROUP_TYPE = (
        ('Individual', 'Individual'),
        ('Group', 'Group of People'),
    )

    ACTIVE_STATUS = (
        ('Active', 'Active'),
        ('In Active', 'In active'),
    )

    spid = models.ForeignKey(User, on_delete=models.CASCADE)
    spname = models.CharField("Service Provider", max_length=50)
    contact = models.CharField(max_length=12)
    email = models.EmailField(blank=True)
    group_type = models.CharField(max_length=20, choices=GROUP_TYPE)
    sp_type = models.CharField("Type of Service", max_length=100)
    experience = models.CharField(
        "Experience details",
        max_length=100,
        blank=True,
        null=True
    )
    specialization = models.TextField(
        "Specialization",
        max_length=100,
        blank=True,
        null=True
    )
    photo = models.ImageField(
        upload_to='images/',
        blank=True,
        null=True
    )
    address = models.TextField(max_length=200)
    from_time = models.TimeField(blank=True)
    to_time = models.TimeField(blank=True)
    twenty_four_hrs = models.BooleanField(default=False)
    service_charge = models.PositiveIntegerField()
    verification_status = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )
    active_status = models.CharField(
        max_length=20,
        choices=ACTIVE_STATUS,
        default='Active'
    )
    created_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.spname


class Servicebooking(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)

    typeofservicereq = models.CharField(max_length=100)
    fromdate = models.DateField(default=date.today)
    todate = models.DateField(blank=True, null=True)

    sp_id = models.PositiveIntegerField(blank=True, default=0)
    sp_name = models.CharField(
        "Service Provider",
        max_length=50
    )

    servicecharge = models.PositiveIntegerField()
    bookingdate = models.DateField(auto_now=True)

    total_days = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    total_amount = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    APPROVALS = (
        ('Approved', 'Approved'),
        ('Not Approved', 'Not Approved'),
        ('Cancelled', 'Cancelled'),
        ('Pending', 'Pending'),
    )

    sbapproval = models.CharField(
        max_length=20,
        choices=APPROVALS,
        default='Not Approved',
        blank=True
    )

    address_remarks = models.TextField(
        max_length=200,
        blank=True
    )

    feedback = models.TextField(
        max_length=100,
        blank=True
    )

    def __str__(self):
        return str(self.username)


class Payment(models.Model):
    sbid = models.OneToOneField(
        Servicebooking,
        on_delete=models.CASCADE
    )

    advance = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    balance = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    discount = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    paidamount = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    credit_to_sp_id = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    credit_to_Self = models.PositiveIntegerField(
        blank=True,
        default=0
    )

    dateof_Transaction = models.DateField(
        default=date.today
    )

    def __str__(self):
        return str(self.sbid)


@receiver(post_save, sender=Servicebooking)
def update_sbid_payment(sender, instance, created, **kwargs):
    if created:
        Payment.objects.create(sbid=instance)

    instance.payment.save()
