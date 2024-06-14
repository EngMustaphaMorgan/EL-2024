#! /usr/bin/python3

#------------------------------------------------------------------------------------------------------------------
# Author      : Mostafa Morgan
# Date        : 13/6/2024
# Description :
#
#
#
#------------------------------------------------------------------------------------------------------------------


# import requests module to get data from a website 
# to get your public ip go to this website
# https://ipinfo.io/json

import requests

def get_public_ip_location(url) :
    
    # Fetch the IP information from ipinfo.io
    response = requests.get(url)

    # parse the json reponse
    data = response.json()

    # extract the relevant information
    ip      = data.get('ip')
    city    = data.get('city')
    region  = data.get('region')
    country = data.get('country')
    loc     = data.get('loc')
    org     = data.get('org')

    # Print the information
    print(f"IP Address: {ip}")
    print(f"Location: {city}, {region}, {country}")
    print(f"Coordinates: {loc}")
    print(f"Organization: {org}")    

get_public_ip_location("https://ipinfo.io/json")