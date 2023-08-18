import requests
from pprint import pprint
SHEETY_PRICE_ENDPOINT = "https://api.sheety.co/98aa8b7b52d7cd5b6b2998c25195ecdd/cheapFLightsDeals/prices"
class DataManager:
    def __init__(self):
        self.destination_data={}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        print(data)
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price" : {
                    "iataCode" : city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPOINT}/{city['id']}",
                json=new_data)
            print(response.text)