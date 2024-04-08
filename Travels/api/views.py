
# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from api.models import Destination,TourPakage,Booking,Review,Tourguide,Activity,Transportation,Payment,Customer,TourSchedule,Invoice,ReviewComment,TourCategory,TourTag
from api.models import Destinationserializers,TourPakageserializers,Bookingserializers,Reviewserializers,Tourguideserializers,Activityserializers,Transportationserializers,Paymentserializers,Customerserializers,TourScheduleserializers,Invoiceserializers,ReviewCommentserializers,TourCategoryserializers,TourTagserializers
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class DestinationViewset(viewsets.ModelViewSet):
    queryset=Destination.objects.all()
    serializer_class=Destinationserializers