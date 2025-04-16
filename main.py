import phonenumbers
number ="+917498151479"
from phonenumbers import geocoder
mobilenumber=phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(mobilenumber,'en'))

from phonenumbers import carrier
serviceprovider=phonenumbers.parse(number,"RO")
print(carrier.name_for_number(serviceprovider,"en"))

from phonenumbers import timezone
phoneNumber=phonenumbers.parse(number)
timeZone=timezone.time_zones_for_number(phoneNumber)
print(timeZone)


