import config
import requests
import openaq

#search_address = "Connaught Place, New Delhi, India"

def googlemap(current_city):
    
    #address = address.replace(" ", "+") 

    #config.load_keys()

    #current_request = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'key='+config.keys["GOOGLE_MAPS"])

    #current_location = current_request.json()
    #print current_location
    
    #if current_location['results']:
    #current_city = current_location['results'][0]['address_components'][1]['long_name']
       # print current_city
        #print "________________________________________________________"
    api = openaq.OpenAQ()
  #  print current_city
    status, resp = api.measurements(city = current_city)
    if status == 200 and resp['results']:
        #print resp['results']
        
        display = resp['results'][0]
        return {"time": display['date']['local'], "city": display['city'], "coordinates": {"lat": display['coordinates']['latitude'], "lng":  display['coordinates']['longitude']}, "location":display['location'], "measurement": {"parameter":display['parameter'], "value":display['value'], "unit": display['unit']}}
    else:
        return {}
#print googlemap(search_address)
