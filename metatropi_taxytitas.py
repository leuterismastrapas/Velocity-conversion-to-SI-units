name_of_unit = "m/s"

def velocity_to_si(given_vel):
    return f"{given_vel} km/h are {(given_vel * 1000)/3600} {name_of_unit}"

user_input = input("Velocity = ?\n")
user_input_number = int(user_input)

calculated_value = velocity_to_si(user_input_number)
print(calculated_value)

