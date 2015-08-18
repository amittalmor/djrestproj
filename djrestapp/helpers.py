from geopy.geocoders import Nominatim

# transform an address string to its coordinates using geopy
def convert_address_to_lat_lon(address):
    if address is None:
        return None,None
    geolocator = Nominatim()
    location = geolocator.geocode(address)
    # geocoding can fail - so be prepared
    lat = getattr(location,'latitude',None)
    lng = getattr(location,'longitude',None)
    return lat,lng
  
# build the address string based on street,city,country
def create_address(data):
    address = ''
    for field in ['street','city','country']:
        address = '%s %s' % (address, data.get(field,''))
    address = address.strip()
    return address

# get or create a GeoAddress object  
def get_or_create_geo_address(lat,lng):
    import models
    #check if such entry exists
    #if yes - just update the count
    #if no - create a new db entry with the relevant data
    qs = models.GeoAddress.objects.filter(latitude=lat,longitude=lng)
    if len(qs) > 0:
        obj = qs[0]
    else:
        obj = models.GeoAddress()
    return obj 