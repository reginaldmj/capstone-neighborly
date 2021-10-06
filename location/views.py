from django.shortcuts import render
from rest_framework import serializers

from location.serializers import NeighborhoodSerializer
from location.models import Neighborhood
from rest_framework.viewsets import ModelViewSet

# Create your views here.

class NeighborhoodViewSet(ModelViewSet):
    queryset = Neighborhood.objects.all()
    serializers_class = NeighborhoodSerializer

URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"
API_KEY = '39129568cfmshbfc46421b214e57p111296jsnbcffc8099e56 '

def get_location(self, request):
    r = request.get(url=URL)



headers = {
    'x-rapidapi-host': "wft-geo-db.p.rapidapi.com",
    'x-rapidapi-key': '39129568cfmshbfc46421b214e57p111296jsnbcffc8099e56 '
    }

response = requests.request("GET", url, headers=headers)

print(response.text)