import requests
from datetime import datetime
import smtplib
import time

MY_lat =19.075983
MY_lng=72.877655
MY_email = "1234@gmail.com"
MY_password = "1234_iitb"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_lat-5<=iss_latitude<=MY_lat+5 and MY_lng-5<=iss_longitude<=MY_lng+5:
        return True

def is_night():
    parameters = {
        "lat": MY_lat,
        "lng": MY_lng,
        "formatted": 0,
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params= parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = data["results"]["sunrise"].split["T"][1].split[":"][0]
    sunset = data["results"]["sunset"].split["T"][1].split[":"][0]

    time_now = datetime.now().hour

    if time_now<= sunrise or time_now>= sunset:
        return True

# while True:
#     time.sleep(60)
#     if is_iss_overhead() and is_night():
#         connection = smtplib.SMTP("smtp.gmail.com")
#         connection.starttls()
#         connection.login(MY_email, MY_password)
#         connection.sendmail(
#             from_addr=MY_email,
#             to_addrs=MY_email,
#             msg="Subject:Look UP \n\n The ISS is above you in the sky."
#         )
