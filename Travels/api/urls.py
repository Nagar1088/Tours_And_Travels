from django.contrib import admin
from django.urls import path,include
from api.views import DestinationViewset,TourPakageViewset,BookingViewset,ReviewViewset,Tourguideviewset,Activityviewset,Transportationviewset,Paymentviewset,customerviewset,TourScheduleviewset,Invoiceviewset,ReviewCommentviewset, TourCategoryviewset,TourTagviewset
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'Destination',DestinationViewset)
router.register(r'TourPakage',TourPakageViewset)
router.register(r'Booking',BookingViewset)
router.register(r'Review',ReviewViewset)
router.register(r'Tourguide',Tourguideviewset)
router.register(r'Activity',Activityviewset)
router.register(r'Transportation',Transportationviewset)
router.register(r'Payment',Paymentviewset)
router.register(r'customer',customerviewset)
router.register(r'TourSchedule',TourScheduleviewset)
router.register(r'Invoice',Invoiceviewset)
router.register(r'ReviewComment',ReviewCommentviewset)
router.register(r' TourCategory',TourCategoryviewset)
router.register(r'TourTag',TourTagviewset)

urlpatterns = [
    path('',include(router.urls)),
]