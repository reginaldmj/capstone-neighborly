from django.shortcuts import render, redirect
# from rest_framework import serializers

from uszipcode import SearchEngine
# from location.serializers import NeighborhoodSerializer
from location.models import Neighborhood
from location. form import NeighorhoodForm
# from rest_framework.viewsets import ModelViewSet

# Create your views here.

# class NeighborhoodViewSet(ModelViewSet):
#     queryset = Neighborhood.objects.all()
#     serializers_class = NeighborhoodSerializer

URL = "https://wft-geo-db.p.rapidapi.com/v1/geo/adminDivisions"
# need a new api_key for google
API_KEY = '39129568cfmshbfc46421b214e57p111296jsnbcffc8099e56 '


# def location_view(request):
#     # ip_address = request.META.get('HTTP_X_FORWARDED_FOR', '')
#     response = requests.get(
#         'https://www.google.com/maps/embed/v1/MAP_MODE?key=API_KEY&parameters' % ip_address)
#     geodata = response.json()
#     return render(request, 'core/home.html', {
#         'city': geodata['city'],
#         'state': geodata['state'],
#         'API_KEY': 'AIzaSyC1UpCQp9zHokhNOBK07AvZTiO09icwD8I'  # Google api_key
#     })


def location_search(request):
    if request.method == 'POST':
        current_user = request.user
        form = NeighorhoodForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_neighborhood = Neighborhood.objects.create(
                zipcode=data['zipcode'],
            )
            engine = SearchEngine()
            results = engine.by_zipcode(data['zipcode'])
            new_neighborhood.city = results.major_city
            new_neighborhood.state = results.state
            new_neighborhood.save()
            current_user.location = new_neighborhood
            current_user.save()
            return render(request, 'map.html', {'results': results, 'current_user': current_user})
    form = NeighorhoodForm()
    return render(request, 'generic_form.html', {'form': form})
