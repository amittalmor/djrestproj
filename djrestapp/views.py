from .models import GeoAddress
from .forms import GeoAddressForm
from .serializers import GeoAddressSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import helpers


def home(request):
    tmpl_vars = {'form': GeoAddressForm()}
    return render(request, 'djrestapp/index.html', tmpl_vars)

@api_view(['POST'])
def post_geoaddress(request):
    if request.method == 'POST':
        # retrieve the user input
        data = {'country': request.data.get('country'),
                'city': request.data.get('city'),
                'street': request.data.get('street'),
                }
        # create an address string
        address = helpers.create_address(data)
        
        # try to convert the address string into coordinates (lat,lng)
        lat,lng = helpers.convert_address_to_lat_lon(address)
        
        # if coordinates do exists, handle the object creation/update
        if lat is not None and lng is not None:
            # update existing object or create a new one
            # the filter is based on the coordinates
            obj = helpers.get_or_create_geo_address(lat,lng)
            if obj.id is not None:
                # updating the object - do not forget to set partial=True 
                partial = True
            else:
                # new object
                partial = False
                data['latitude'] = lat
                data['longitude'] = lng
            
            # increment the number of visits
            data['count'] = obj.count + 1
            
            # use serialzer to save the object
            serializer = GeoAddressSerializer(obj,data=data,partial=partial)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            # on serializtion error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # on google conversion error
        return Response(status=status.HTTP_400_BAD_REQUEST)



