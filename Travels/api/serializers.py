from rest_framework import serializers
from api.models import Destination,TourPakage,Booking,Review,Tourguide,Activity,Transportation,Payment,Customer,TourSchedule,Invoice,ReviewComment,TourCategory,TourTag



class Destinationserializers(serializers.HyperlinkedModelSerializer):
    Destination=serializers.ReadOnlyField()
    class Meta:
        model=Destination
        fields='__all__'


class TourPakageserializer(serializers.HyperlinkedModelSerializer):
    TourPakage=serializers.ReadOnlyField()
    class Meta:
        model=TourPakage
        fields='__all__'


class Bookingserializers(serializers.HyperlinkedModelSerializer):
    Booking=serializers.ReadOnlyField()
    class Meta:
        model=Booking
        fields='__all__'


class Reviewserializers(serializers.HyperlinkedModelSerializer):
    Review=serializers.ReadOnlyField()
    class Meta:
        Model=Review
        fields='__all__'


class Tourguideserializers(serializers.HyperlinkedModelSerializer):
    Tourguider=serializers.ReadOnlyField()
    class Meta:
        model=Tourguide
        fields='__all'


class Activityserializers(serializers.HyperlinkedModelSerializer):
    Activity=serializers.ReadOnlyField()
    class Meta:
        model=Activity
        fields='__all__'


    
class Transportationserializers(serializers.HyperlinkedModelSerializer):
    Transportation=serializers.ReadOnlyField()
    class Meta:
        model=Transportation
        fields='__all__'


class paymentserializers(serializers.HyperlinkedModelSerializer):
    Payment=serializers.ReadOnlyField()
    class Meta:
        model=Payment
        fields='__all__'


class Customerserializers(serializers.HyperlinkedModelSerializer):
    Customer=serializers.ReadOnlyField()
    class Meta:
        model=Customer
        fields='__all__'


class TourScheduleserializers(serializers.HyperlinkedModelSerializer):
    Tourshedule=serializers.ReadOnlyField()
    class Meta:
        model=TourSchedule
        fields='__all__'


class Invoiceserializers(serializers.HyperlinkedModelSerializer):
    Invoice=serializers.ReadOnlyField()
    class Meta:
        model=Invoice
        fields='__all__'


class ReviewCommentserializers(serializers.HyperlinkedModelSerializer):
    Review=serializers.ReadOnlyField()
    class Meta:
        model=Review
        fields='__all__'


class TourCategoryserializers(serializers.HyperlinkedModelSerializer):
    Tourcategory=serializers.ReadOnlyField()
    class Meta:
        model=TourCategory
        fields='__all__'


class TourTagserializers(serializers.HyperlinkedModelSerializer):
    TourTag=serializers.ReadOnlyField()
    class Meta:
        model=TourTag
        fields='__all__'
    
