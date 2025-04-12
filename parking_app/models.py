from django.db import models


class User(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.username

class Guard(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Mall or location name
    contact = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class ParkingRequest(models.Model):
    user_query = models.CharField(max_length=255)
    guard_reply = models.TextField(blank=True)  # Guard replies manually
    timestamp = models.DateTimeField(auto_now_add=True)
    guard = models.ForeignKey(Guard, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"Request: {self.user_query} | Guard: {self.guard.name if self.guard else 'None'}"

class ParkingSpot(models.Model):
    name = models.CharField(max_length=100)  # Name of the parking spot
    location = models.CharField(max_length=255)  # Location description
    is_available = models.BooleanField(default=True)  # Availability status
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)  # Price per hour

    def __str__(self):
        return self.name  # Display the name in admin interface
