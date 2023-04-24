"""
* Assignment 5
* Xueyao Wang
* Fetching the Weather
* Sample output:
*  [{'air_pressure': 993.23,
  'air_quality': 67.01,
  'ambient_temp': -14.02,
  'created_by': 'MCC Weather Station',
  'created_on': '2019-01-09T12:24:32Z',
  'ground_temp': -8.63,
  'humidity': 44.22,
  'id': 15124415,
  'rainfall': 0,
  'reading_timestamp': '2019-01-09T12:24:32Z',
  'updated_by': 'MCC Weather Station',
  'updated_on': '2019-01-09T18:33:09.919Z',
  'weather_stn_id': 3528546,
  'wind_direction': 234.06,
  'wind_gust_speed': 12.97,
  'wind_speed': 9.38}]

"""

from requests import get
import json
from pprint import pprint
from haversine import haversine


stations = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getallstations'
weather = 'https://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/'


my_lat = 49.900011
my_lon = -97.140833

all_stations = get(stations).json()['items']


def find_closest() -> int:
    """Find the closest weather station to your location"""

    smallest = 20036
    for station in all_stations:
        station_lon = station['weather_stn_long']
        station_lat = station['weather_stn_lat']
        distance = haversine(my_lon, my_lat, station_lon, station_lat)
        if distance < smallest:
            smallest = distance
            closest_station = station['weather_stn_id']
    return closest_station


closest_stn = find_closest()


weather = weather + str(closest_stn)


my_weather = get(weather).json()['items']
pprint(my_weather)
