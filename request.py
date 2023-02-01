import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'count_in_your_room':5, 'hotel_star_rating':2})

print(r.json())


