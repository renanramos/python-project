import requests
import json

# print("200 is a great number")
# print(2)

# print()
############################

def days_to_units(num_of_days) :
    calculation_to_units = 24 * 60 * 60
    name_of_unit = "seconds"
    print(f"{num_of_days} days are {calculation_to_units * num_of_days} {name_of_unit}")

days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(110)
