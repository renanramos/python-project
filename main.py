calculation_to_units = 24
name_of_unit = "hours"
user_input = ""

def days_to_units(num_of_days) :
    return f"{num_of_days} days are {calculation_to_units * num_of_days} {name_of_unit}"

def validate_and_execute():
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print(f"you entered {user_input_number}, please enter a valid positive number")
        else:
            print(f"you entered {user_input_number}, no conversion for you")
    except ValueError:
        print(f"your input '{num_of_days_element}' is not a number. Do not ruin my program!")

while user_input != "exit" :
    user_input = input("Hey user, enter number of days as comma separated list and I will convert it to hours!\n")
    for num_of_days_element in user_input.split(", "):
        validate_and_execute()