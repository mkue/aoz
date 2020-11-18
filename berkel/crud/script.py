from berkel.wsgi import application
from crud.models import Customer

print("""
    1. Customer erstellen
""")

user_input = int(input('Was möchtest du machen?'))

if user_input == 1:
    first_name = input('Vorname: ')
    last_name = input('Nachname: ')
    age = int(input('Alter: '))
    Customer(first_name=first_name, last_name=last_name, age=age).save()
