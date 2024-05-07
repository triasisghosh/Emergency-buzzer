#.A Safety Buzzer that will trigger a alarm and send alert SMS along with your location to family/friends

from twilio.rest import Client #twilio api is used for sending SMS
import tkinter as tk #for GUI
from pygame import mixer #to play the alarm
import csv #handles .csv file
import requests
import json #handles .json file

#this .json file contains credentials for ipapi and twilio
f=open('Access_keys.json')
key=json.load(f)

#return location url
def ip_ret():
    ipapi_access_key = key['ipapi']
    url = f"http://api.ipapi.com/check?access_key={ipapi_access_key}&output=json/"
    geo_j=requests.get(url)
    geo_j=geo_j.json()
    inf=f"\nIP address: {geo_j['ip']}" \
        f"\nPIN code: {geo_j['zip']}" \
        f"\nCity: {geo_j['city']}" \
        f"\nState: {geo_j['region_name']}" \
        f"\nCountry: {geo_j['country_name']}" \
        f"\nGeoname id: {geo_j['location']['geoname_id']}" \
        f"\nLatitude: {geo_j['latitude']}" \
        f"\nLongitude: {geo_j['longitude']}" \
        f"\n\nGoogle map Link: https://www.google.com/maps/search/?api=1&query={geo_j['latitude']}%2C{geo_j['longitude']}&authuser=1"
    return inf

#send sms to saved numbers
def send_sms():
    f=open("contact.csv","r")
    list=csv.reader(f)
    num=""
    tw_sid=key['twilio_sid']
    tw_auth=key['twilio_auth_id']
    for row in list:
        num=num.join(row)
        client=Client(tw_sid,tw_auth)
        client.messages.create(to=('+91'+num),from_=f"+14355710253",body=f"Help please, I am in trouble. Here is my location:\n{ip_ret()}")
    f.close()

#play buzzer sound and send sms
def buzzer_fn():
    mixer.init()
    mixer.music.load("electric-buzz.wav")
    mixer.music.play(loops=10)
    mixer.music.set_volume(1.0)
    send_sms()

#making the tkinter window for GUI
buzz=tk.Tk()
buzz.geometry("600x500")
buzz.title("Emergency Buzzer")

#label
fnt=("Ariel",20,"bold")
label=tk.Label(buzz,text="EMERGENCY BUZZER!!!",fg='Red',font=fnt)
label.pack()

#buzzer button
bi=tk.PhotoImage(file="buzzer_img.png")
buzzer=tk.Button(buzz,image=bi,borderwidth=0,command=buzzer_fn)
buzzer.pack()

# label
fnt = ("Ariel", 20, "italic")
label = tk.Label(buzz, text="Police: 100    Ambulance: 102\nWomen helpline: 1091    Fire Brigade: 101", fg='Red', font=fnt,pady=-10)
label.pack()

buzz.mainloop()
