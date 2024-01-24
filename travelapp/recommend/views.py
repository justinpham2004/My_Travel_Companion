from django.shortcuts import render
from .models import *
from django.http import Http404

from .library import google_maps, recommend_ai, yelp_fusion
### Local Methods ###


# Create your views here.
def main(request):
    context = {}
    
    return render(request, 'recommend/main.html', context)

#def buttonpress(request):
#   if request.method == 'POST':

def displayresults(request):
   try: 
        if request.method == 'POST':
            prompt = request.POST.get('vacationPrompt') or "No Response Entered"

            ##find way to organize data with models ##
            
            ## city data ##
            parse = recommend_ai.parse_response(prompt) 
            
            ## itinerary ##
            itinerary = recommend_ai.create_itinerary(address = parse[0], stay = parse[1], age = parse[2])
           
            ## city description ##
            city = parse[0]
            city_description = recommend_ai.location_description(parse[0])
            #print(parse)

            #print(city, city_description, itinerary)
            
            ## generate yelp content ##
            #yelp_request = yelp_fusion.get_business_ids(term = 'restaurants', #location = parse[0])
            #print(yelp_request)

            restaurants = []
            reviews = []
            #for business_id in yelp_request:
                #restaurants.append(yelp_fusion.get_business(business_id))
                #reviews.append(yelp_fusion.get_business_reviews[0])
            
            ## add to context ##
            """"
            context = {
                'city' : city,
                'city_description' : city_description,
                'restaurants' : restaurants,
                'reviews' : reviews,
                'itinerary': itinerary
            
            } 
            """
            # Extract customer id, input actual id of user
            # customer = Customer.objects.get(pk = customer_id)
            #recommendation = customer.recommendation
            
            #get relevant data
            context = {
                'customer': 'justin',
                'city': 'tokyo',
                'itineraries': 'go here!!',
                'restaurants': 'mcdonalds'
            }
            print(context)
            
            return render(request, 'recommend/displayresults.html', context)
                


        



        
   except:
       raise Http404("Oops! Something went wrong")
