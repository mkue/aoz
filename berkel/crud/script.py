from berkel.wsgi import application
from crud.models import Customer

print("""
    1. Customer erstellen
    2. Customer Liste
    3. Customer Detail
    4. Customer Aktualisieren
    5. Customer Löschen
    6. Customer Suchen
""")

user_input = int(input('Was möchtest du machen?'))

if user_input == 1:
    first_name = input('Vorname: ')
    last_name = input('Nachname: ')
    age = int(input('Alter: '))
    Customer(first_name=first_name, last_name=last_name, age=age).save()

elif user_input == 2:
    all_entries = Customer

    all_entries = sorted(all_entries)
    for entity in all_entries:
        print(entity.id)
        print(entity.first_name + " - " + entity.last_name + " - " + str(entity.age))
        print(entity)

elif user_input == 3:
    id = int(input("Bitte, Sie schreiben Id: "))
    model = Customer()
    model.
    entity = Customer.objects.get(pk=id)

# elif user_input == 4:
# input_text = input("Bitte, Sie schreiben : ")
# entity = Customer.objects.filter(first_name=input_text)
# first_name = input('Vorname: ')
# last_name = input('Nachname:  ')
# age = int(input('Alter: '))
# entity.first_name = first_name
# entity.last_name = last_name
# entity.age = age
# entity.save()
elif user_input == 5:

    id = int(input("Bitte, Sie schreiben Id: "))
    entity = Customer.objects.get(pk=id)
    entity.delete()


elif user_input == 6:
    input_text = input("Bitte, Sie schreiben : ")
    all_entries = Customer.objects.filter(first_name=input_text)
    #  = Customer.objects.filter(last_name=input_text)
    for entity in all_entries:
        print(entity)

#
