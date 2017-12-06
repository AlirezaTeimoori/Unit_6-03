#Created by: Alireza Teimoori
#Created on: Dec 2017
#Created for: ICS3UR-1
#Lesson: Unit 6-03
#This program shows mailing address


class Mailing_address():
    def __init__(self, first_name, last_name, street_number, city_name, province, postal_code):
        self.first_name = first_name
        self.last_name = last_name
        self.street_number = street_number
        self.city_name = city_name
        self.province = province
        self.postal_code = postal_code

user = Mailing_address(raw_input("Enter your first name: \n"), raw_input("Enter your last name: \n"), raw_input("Enter your street_number: \n"), raw_input("Enter your city name: \n"), raw_input("Enter your province: \n"), raw_input("Enter your postal code: \n"))

print("\n\n")
print(user.first_name+" "+user.last_name)
print("10-123 1/2 "+user.street_number)
print(user.city_name+" "+user.province+" "+user.postal_code)

