import requests
from twilio.rest import Client
account_sid = 'AC79337853a95a60a6d252e2e18fc0XXXX'
auth_token = 'b2604a76bdfece73aefef7ff9c72XXXX'

api_key="016ea5d6a95add4cebf64025bb989103"
api="https://api.openweathermap.org/data/2.5/forecast"

parameters={
    "lat":25.286295,
    "lon":55.427929,
    "appid": api_key,
    "cnt":4
}
response=requests.get(url=api,params=parameters)
data=response.json()
# ["list"][0]["weather"][0]["id"]
print(response)
# print(data)
will_rain =False
for hour_data in data["list"] :
    code=hour_data["weather"][0]["id"]
    if code<700 :
        will_rain=True

if will_rain:
    print("Dont forget to take umbrella with you !")
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Don’t forget to take an umbrella with you! It may rain .',
        from_='whatsapp:+141XXXXXXXX',  # Twilio Sandbox number
        to='whatsapp:+9190XXXXXXXX'  # Your verified number that joined the sandbox
    )

    print(message.sid)

else :
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Yo ! Its Hot outside ☀️🥵 .Make sure you apply sunscreen before heading out 🧴 \n Saisha would be thirsty Ask her if she needs some water ',
        from_='whatsapp:+141XXXXXXXX',  # Twilio Sandbox number
        to='whatsapp:+9190XXXXXXXX'  # Your verified number that joined the sandbox
    )

    print(message.sid)




