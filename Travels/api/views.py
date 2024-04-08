
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Destination,TourPakage,Booking,Review,Tourguide,Activity,Transportation,Payment,Customer,TourSchedule,Invoice,ReviewComment,TourCategory,TourTag
from api.serializers import Destinationserializers,TourPakageserializers,Bookingserializers,Reviewserializers,Tourguideserializers,Activityserializers,Transportationserializers,Paymentserializers,Customerserializers,TourScheduleserializers,Invoiceserializers,ReviewCommentserializers,TourCategoryserializers,TourTagserializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class DestinationViewset(viewsets.ModelViewSet):
    queryset=Destination.objects.all()
    serializer_class=Destinationserializers

class TourPakageViewset(viewsets.ModelViewSet):
    queryset=TourPakage.objects.all()
    serializer_class=TourPakageserializers

class BookingViewset(viewsets.ModelViewSet):
    queryset=Booking.objects.all()
    serializer_class=Bookingserializers

class ReviewViewset(viewsets.ModelViewSet):
    queryset=Review.objects.all()
    serializer_class=Reviewserializers


class Tourguideviewset(viewsets.ModelViewSet):
    queryset=Tourguide.objects.all()
    serializer_class=Tourguideserializers


class Activityviewset(viewsets.ModelViewSet):
    queryset=Activity.objects.all()
    serializer_class=Activityserializers


class Transportationviewset(viewsets.ModelViewSet):
    queryset=Transportation.objects.all()
    serializer_class=Transportationserializers


class Paymentviewset(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=Paymentserializers


class customerviewset(viewsets.ModelViewSet):
    queryset=Customer.objects.all()
    serializer_class=Customerserializers


class TourScheduleviewset(viewsets.ModelViewSet):
    queryset=TourSchedule.objects.all()
    serializer_class=TourScheduleserializers


class Invoiceviewset(viewsets.ModelViewSet):
    queryset=Invoice.objects.all()
    serializer_class=Invoiceserializers


class ReviewCommentviewset(viewsets.ModelViewSet):
    queryset=ReviewComment.objects.all()
    serializer_class=ReviewCommentserializers


class TourCategoryviewset(viewsets.ModelViewSet):
    queryset=TourCategory.objects.all()
    serializer_class=TourCategoryserializers


class TourTagviewset(viewsets.ModelViewSet):
    queryset=TourTag.objects.all()
    serializer_class=TourTagserializers





