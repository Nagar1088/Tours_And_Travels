from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User



class Destination(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.ImageField(upload_to='Destination_image')

    def __str__(self):
        return self.name
    class Meta:
        managed=True
    

class TourPakage(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    destinations = models.ManyToManyField(Destination)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration = models.PositiveIntegerField(help_text='Duration in days')

    def __str__(self):
        return self.title
    class Meta:
        managed=True
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour_package = models.ForeignKey(TourPakage, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}'s booking for {self.tour_package.title}"
    class Meta:
        managed=True


class Review(models.Model):
    tour_package = models.ForeignKey(TourPakage, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=((1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')))
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.tour_package.title} by {self.user.username}"
    class Meta:
        managed=True



class Tourguide(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to='guide_images')

    def __str__(self):
        return self.name
    class Meta:
        managed=True
    

class Activity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tour_package = models.ForeignKey(TourPakage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        managed=True
    

class Transportation(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    tour_package = models.ForeignKey(TourPakage, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    class Meta:
        managed=True
    

class Payment(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment for {self.booking}"
    class Meta:
        managed=True
    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    class Meta:
        managed=True
    

class TourSchedule(models.Model):
    tour_package = models.ForeignKey(TourPakage, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.tour_package.title} - {self.start_date} to {self.end_date}"
    class Meta:
        managed=True



class Invoice(models.Model):
    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    issue_date = models.DateField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return f"Invoice for {self.booking} - Amount: {self.amount}"
    class Mate:
        managed=True


class ReviewComment(models.Model):
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment on {self.review} by {self.user.username}"
    class mate:
        managed=True


class TourCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        managed=True
    

class TourTag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    class Meta:
        managed=True