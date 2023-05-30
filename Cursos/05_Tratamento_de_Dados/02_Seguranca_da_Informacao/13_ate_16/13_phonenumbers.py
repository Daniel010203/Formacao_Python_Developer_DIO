import phonenumbers
from phonenumbers import geocoder

phone = input('Digite um telefone no formato: (Ex: +551199800123): ')

phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))