from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True, blank = True)
    prompt_response = models.CharField(max_length = 400, null = True)
    city = models.CharField(max_length = 200, null = True)
    stay_len = models.CharField(max_length = 20, null = True)
    age = models.CharField(max_length = 200, null = True)
    email = models.CharField(max_length = 200, null = True)

    def __str__(self):
        return  self.email

class Recommendation(models.Model):
    
    ### Linkage to Customer ###
    customer = models.OneToOneField(Customer, on_delete = models.CASCADE)

    ### Functions to display results ###
    def restaurants(self):
        return Restaurant.objects.filter(recommendation = self)
    def itineraries(self):
        return Itinerary.objects.filter(Recommendation = self)



### Possibly Change such that there can be multiple iteneraries per day? ###
class Itinerary(models.Model):
    ### Linkage to Recommendation Model ###
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)

    ### Details of Itinerary
    
    itenerary = models.CharField(max_length = 400, null = True)

class City(models.Model):
    ### Linkage to Recommendation Model ###
    recommendation = models.OneToOneField(Recommendation, on_delete = models.CASCADE)
    
    ### City Details ###
    city = models.CharField(max_length = 200, null = True)
    description = models.CharField(max_length = 200, null = True)

class Restaurant(models.Model):
    ### Linkage to Recommendation Model ###
    recommendation = models.ForeignKey(Recommendation, on_delete = models.CASCADE)

    ### Restaurant Details ###
    name = models.CharField(max_length = 255)
    address = models.CharField(max_length=255)
    review_summary = models.TextField(blank=True)
    website_link = models.URLField(blank=True)
    image_url = models.URLField(blank=True)
    price = models.CharField(max_length = 200)


#there can be mulitple restaurant recommendations for one restauratn
#remember to ask google to return a JSON for three daily iteneraries i gues..