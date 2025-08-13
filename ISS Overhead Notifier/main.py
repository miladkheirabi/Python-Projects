import requests
from datetime import datetime
import smtplib

MY_EMAIL=your_email@example.com
MY_PASSWORD=your_app_password
MY_LAT= your_latitude
MY_LONG= your_longitude


minute = 0
while 1:
    time_now = datetime.now()
    if time_now.minute != minute:
        minute = time_now.minute
        try:
            response = requests.get(url="http://api.open-notify.org/iss-now.json")
        except:
            print("connection error")
        else:
            data = response.json()

            iss_latitude = float(data["iss_position"]["latitude"])
            iss_longitude = float(data["iss_position"]["longitude"])

            #Your position is within +5 or -5 degrees of the ISS position.

            parameters = {
                "lat": MY_LAT,
                "lng": MY_LONG,
                "formatted": 0,
            }

            response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
            response.raise_for_status()
            data = response.json()
            sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
            sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

            #If the ISS is close to my current position
            if 46 < iss_longitude < 56 and 30 < iss_latitude < 40:
                # and it is currently dark
                if sunset < time_now.hour or time_now.hour < sunrise:
                    # Then send email to tell me to look up.
                    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as connection:
                        connection.login(MY_EMAIL, password=PASSWORD)
                        connection.sendmail(from_addr=MY_EMAIL, to_addrs="miladkheirabi@gmail.com",
                                            msg=f"subject:LOOK UP!")
    # BONUS: run the code every 60 seconds.



