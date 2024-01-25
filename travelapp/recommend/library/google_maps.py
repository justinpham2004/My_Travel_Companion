

##This file will be for all function calls related to displaying google maps on places, etc. as well as directions and such
import googlemaps
from pprint import pprint
import pandas as pd

#google maps api key; 
API_KEY = 'HIDDEN'
map_client = googlemaps.Client(API_KEY)

#work_place_address = ' 1 Market st, San Francisco, CA'
#Aresponse = map_client.geocode(work_place_address)
#pprint(response)

#This file will be a library for setting up the google maps API,
#getting distance from the current location
#displaying on maps the current pins

#given restaurant suggestions, will provide restaurant directions in the form of a url
#note that origin is replaced
def get_direction_url(origin, destination):
    addr1 = origin.replace(' ', '+')
    addr2 = destination.replace(' ', '+')
    #print(addr1 + addr2)
    return 'https://www.google.com/maps/dir/{addr1}/{addr2} '.format(addr1 = addr1, addr2 = addr2)




##FUTURE FUNCTIONALITY
def add_to_map():
    return

def add_all_to_map():
    return

#print(get_direction_url("12612 Bright Spring Way, Boyds, MD, 20841", "McDonald's, 21121 Frederick Rd, Germantown, MD 20876"))
