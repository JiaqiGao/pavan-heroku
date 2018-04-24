import config
import requests
import openaq

#search_address = "Connaught Place, New Delhi, India"

def googlemap(address):
    address = address.replace(" ", "+") 

    config.load_keys()

    current_request = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'key='+config.keys["GOOGLE_MAPS"])

    current_location = current_request.json()

    if current_location['results']:
        current_city = current_location['results'][0]['address_components'][1]['long_name']
        api = openaq.OpenAQ()
        status, resp = api.measurements(city = current_city)
        display = resp['results'][0]
        return {"time": display['date']['local'], "city": display['city'], "location":display['location'], "measurement": {"parameter":display['parameter'], "value":display['value'], "unit": display['unit']}}
    else:
        return {} 
