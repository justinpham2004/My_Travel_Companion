
import json
import requests
import sys
import urllib
import argparse
import pprint

#ERROR HANDLING FOR HTML
try:
    # For Python 3.0 and later
    from urllib.error import HTTPError
    from urllib.parse import quote
    from urllib.parse import urlencode
except ImportError:
    # Fall back to Python 2's urllib2 and urllib
    from urllib import quote
    from urllib import urlencode

### NOTE: 
##YELP API KEY: 
##YELP CLIENT  ID: UENU3qwROQIQQzu2EYLemg

from yelp.client import Client

#My API Key
API_KEY = 'HIDDEN'
client = Client(API_KEY)

#API Constnats
API_HOST = 'https://api.yelp.com'
SEARCH_PATH = '/v3/businesses/search'
BUSINESS_PATH = '/v3/businesses/'  # Business ID will come after slash.


# Defaults for our simple example.
DEFAULT_TERM = 'Restaurants'
DEFAULT_LOCATION = '12612 Bright Spring Way, Boyds, MD, 20841'
SEARCH_LIMIT = 10

#########################API REQUEST##########################

##SENDING REQUEST

"""Given your API_KEY, send a GET request to the API.

    Args:
        host (str): The domain host of the API.
        path (str): The path of the API after the domain.
        API_KEY (str): Your API Key.
        url_params (dict): An optional set of query parameters in the request.

    Returns:
        dict: The JSON response from the request.

    Raises:
        HTTPError: An error occurs from the HTTP request.
    """
def request(host, path, api_key, url_params = None):
    #{0}{1} is like format specifiers in C strings
    #encode encodes it for compatibility
    #quote adds quotations so it is compatible to be concatted
    url_params  = url_params or {}
    url = '{0}{1}'.format(host, quote(path.encode('utf8')))
    headers = {
        'Authorization': 'Bearer %s' % api_key ##wtf is this for????!
    }

    #indicating request being made
    print(u'Querying {0} ...'.format(url))

    response = requests.request('GET', url, headers = headers, params = url_params)

    return response.json()


def search(api_key, term, location):
    """Query the Search API by a search term and location.

    Args:
        term (str): The search term passed to the API.
        location (str): The search location passed to the API.

    Returns:
        dict: The JSON response from the request.
    """
    url_params = {
        'term': term.replace(' ', '+'),
        'location': location.replace(' ', '+'),
        'limit': SEARCH_LIMIT
    }
    return request(API_HOST, SEARCH_PATH, api_key, url_params=url_params)





########################PARSING RESPONSE DATA###########################


##RETRIEVING DATA
def get_business( business_id):
    """Query the Business API by a business ID.
    Args:
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    #second get request after the first
    business_path = BUSINESS_PATH + business_id
    return request(API_HOST, business_path, API_KEY)


def get_business_ids(term, location):
    """Queries the API by the input values from the user.

    Args:
        term (str): The search term to query.
        location (str): The location of the business to query.
    """
    business_ids = []
    response = search(API_KEY, term, location)
    businesses = response.get('businesses')
    
    ##   business_ids.append(business['id'])
    print(businesses[0]['id'])
    for i in range (0, len(businesses)):
        business_ids.append(businesses[i]['id'])
    
    print(business_ids)
    return business_ids


def get_business_reviews(business_id):
    """Queries the API for a business's reviews..
    Args:
        api_key: The API key of the user
        business_id (str): The ID of the business to query.

    Returns:
        dict: The JSON response from the request.
    """
    review_path = '/v3/businesses/{0}/reviews'.format(business_id)
    

    return request(API_HOST, review_path, API_KEY)

#def main():
    
    ## In case I want to use command line arguments ##
    ##parser = argparse.ArgumentParser()

    """parser.add_argument('-q', '--term', dest='term', default=DEFAULT_TERM,
                        type=str, help='Search term (default: %(default)s)')
    parser.add_argument('-l', '--location', dest='location',
                        default=DEFAULT_LOCATION, type=str,
                        help='Search location (default: %(default)s)') """

    """input_values = parser.parse_args()
    print(input_values)"""

    #try:
        #query_api(input_values.term, input_values.location)
        #business_ids = get_business_ids(DEFAULT_TERM, DEFAULT_LOCATION)
        #print(get_business(API_KEY, business_ids[0])['name'])
        #print(get_business_reviews(API_KEY, business_ids[0]))

    #except HTTPError as error:
        #sys.exit(
            #'Encountered HTTP error {0} on {1}:\n {2}\nAbort program.'.format(
                #error.code,
                #error.url,
                #error.read(),
            #)
        #)


#if __name__ == '__main__':
    
    #main()
