## This file will be for configuring api requests to the ai

#api key for Gemini: AIzaSyA6YBiTi4GbKZB6-pu1f7HoALNKmxJc5pM

#in the future, read text from a document, and use ML to automate its deciphering/with a given prompt!!

import google.generativeai as genai

# Used to securely store your API key

##THIS IS AN IMPORTANT POSSIBILITY 

#Setup API
GOOGLE_API_KEY= 'AIzaSyA6YBiTi4GbKZB6-pu1f7HoALNKmxJc5pM'
genai.configure(api_key=GOOGLE_API_KEY)

#API
model = genai.GenerativeModel('gemini-pro')
#response = model.generate_content("give me a list of 8 highly rated restaurants of japanese cuisines near Shinjuku, Japan, along with a short description of what food they cook, and a link to their restaurant. Use the JSON format given below ['restaurant' : 'Kozue', 'description' : 'A delicious dipping ramen', 'website' : 'https://restaurants.tokyo.park.hyatt.co.jp/en/koz.html']")


def create_itinerary(stay, age, address):
    response = model.generate_content("Give me a {0}-day itinerary for a {1} staying in {2}".format(stay, age, address))

    return response.text

def location_description(city):
    response = model.generate_content("Give me a one sentence description of this {city} that is under 400 characters".format(city = city))

    return response.text

def parse_response(input):
    parse = model.generate_content("Parse this response into an array such that array[0] is the city where the user is staying, array[1] is the length of their city, array[2] is their age, and array[3] is the most accurate address provided. The response is as given: {response}".format(response = input))

    return parse.text

#parse_response("I will be staying in Tokyo for 5 days, I love eating japanese food and I am really excited for this trip. and I am a 20 year old student")
#print(location_description("Tokyo"))



#print(create_itenerary(2, 56, "Kyoto Station, Kyoto"))