def classify_hurricane(wind_speed):
    """Classifies the wind speed based on the Saffir-Simpson Hurricane Scale."""
    if wind_speed < 0:
        return "Error: Wind speed cannot be negative."
    elif wind_speed < 39:
        return "Not a tropical storm or hurricane."
    elif wind_speed <= 73:
        return "Tropical Storm."
    elif wind_speed <= 95:
        return "Category 1: Very dangerous winds will produce some damage."
    elif wind_speed <= 110:
        return "Category 2: Extremely dangerous winds will cause extensive damage."
    elif wind_speed <= 129:
        return "Category 3: Devastating damage will occur."
    elif wind_speed <= 156:
        return "Category 4: Catastrophic damage will occur."
    else:
        return "Category 5: Catastrophic damage; high devastation."

while True:
    try:
        speed = int(input("Enter the wind speed in mph: "))
        print(classify_hurricane(speed))
        break
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
