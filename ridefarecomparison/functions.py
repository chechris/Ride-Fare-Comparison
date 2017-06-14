import requests

def getUberPrice(start_latitude, start_longitude, end_latitude, end_longitude, SeatCount):
    params = {'start_latitude':start_latitude, 'start_longitude': start_longitude, 'end_latitude':end_latitude, 'end_longitude': end_longitude, 'SeatCount': SeatCount}
    uberPrice = requests.get('https://api.uber.com/v1.2/estimates/price', params=params)
