# Emergency-buzzer
A simple buzzer that will trigger an alarm and send alert SMS to the family/friends along with the location.

# Manual for users
* Add the required phone numbers in the contact.csv file without country code.
  Don't keep any other text in that file or put comma, simply add phone numbers in newlines.
* After running the program press the buzzer and see.

# Instruction for coders
* Add the required credentials inside the .json file in specified places.
* If you use free version of Twilio, you need to register and verify a number in your [console at twilio](https://console.twilio.com)
  so you can send SMS to the number. With premium account there is no such rule. Also remember with free account you get only $15 which will be
  spent on sending SMS's.
* If you use free version of ipapi, you will get only 1000 request processing per month. There are many types of premium plans with different limits.

# Dependencies
1. Twilio API
2. ipapi API
3. Tkinter
4. Pygame

# Code description
1. ip_ret() function returns the location data by ipapi API. Location data contains IP address, PIN code, city,
   state, country, latitude, longitude and G-map link for that latitude and longitude.
2. send_sms() function sends SMS to the numbers stored in "contact.csv" file along with the location returned by ip_ret().
3. buzzer_fn() triggers "electric-buzz.wav" audio file by using mixer module of pygame and calls send_sms().
4. GUI window with the buzzer button is made with tkinter.

# Files in root directory of program
* "Access_keys.json": This file contains all credentials of ipapi and twilio API used in program.
* "contact.csv": This file contains the emergency phone numbers, where alerts to be sent on pressing buzzer.
* "buzzer_img.png": The image of buzzer button.
* "electric-buzz.wav": Audio file containing buzzer sound.

**Please feel free to contribute in this project. This is a concept project, it need to be implemented in Android/iOS platform or
in web-application for realtime use. Also instead of IP tracking, GPS need to be implemented for better accuracy.** 

# Reach me
* instagram @triasisghosh
* linkedin at https://www.linkedin.com/in/triasis-ghosh-322b27201
