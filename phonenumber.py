import phonenumbers

from test import number # from test.py file importing that phonenumber

from phonenumbers import geocoder #geocoder is for country loaction 
ch_nmber = phonenumbers.parse(number , "CH") # created a variable country number and parse the parameters inside number and country history
print(geocoder.description_for_number(ch_nmber, "en")) # print the number in language english using geocoder with country name

# now to print service provider of that phone number

from phonenumbers import carrier # carrier is for service provider name
service_number = phonenumbers.parse(number, "RO")
print(carrier.name_for_number(service_number, "en")) # print carrier name in english

