import matplotlib.pyplot as plt
from PIL import Image

# Complete dictionary of all U.S. states
states_data = {
    "Alabama": {"capital": "Montgomery", "population": 4903185, "flower": "Camellia"},
    "Alaska": {"capital": "Juneau", "population": 731545, "flower": "Forget-me-not"},
    "Arizona": {"capital": "Phoenix", "population": 7278717, "flower": "Saguaro Cactus Blossom"},
    "Arkansas": {"capital": "Little Rock", "population": 3017804, "flower": "Apple Blossom"},
    "California": {"capital": "Sacramento", "population": 39512223, "flower": "California Poppy"},
    "Colorado": {"capital": "Denver", "population": 5758736, "flower": "Rocky Mountain Columbine"},
    "Connecticut": {"capital": "Hartford", "population": 3565287, "flower": "Mountain Laurel"},
    "Delaware": {"capital": "Dover", "population": 973764, "flower": "Peach Blossom"},
    "Florida": {"capital": "Tallahassee", "population": 21477737, "flower": "Orange Blossom"},
    "Georgia": {"capital": "Atlanta", "population": 10617423, "flower": "Cherokee Rose"},
    "Hawaii": {"capital": "Honolulu", "population": 1415872, "flower": "Hibiscus"},
    "Idaho": {"capital": "Boise", "population": 1787065, "flower": "Syringa"},
    "Illinois": {"capital": "Springfield", "population": 12671821, "flower": "Violet"},
    "Indiana": {"capital": "Indianapolis", "population": 6732219, "flower": "Peony"},
    "Iowa": {"capital": "Des Moines", "population": 3155070, "flower": "Wild Prairie Rose"},
    "Kansas": {"capital": "Topeka", "population": 2913314, "flower": "Sunflower"},
    "Kentucky": {"capital": "Frankfort", "population": 4467673, "flower": "Goldenrod"},
    "Louisiana": {"capital": "Baton Rouge", "population": 4648794, "flower": "Magnolia"},
    "Maine": {"capital": "Augusta", "population": 1344212, "flower": "White Pine Cone and Tassel"},
    "Maryland": {"capital": "Annapolis", "population": 6045680, "flower": "Black-Eyed Susan"},
    "Massachusetts": {"capital": "Boston", "population": 6892503, "flower": "Mayflower"},
    "Michigan": {"capital": "Lansing", "population": 9986857, "flower": "Apple Blossom"},
    "Minnesota": {"capital": "St. Paul", "population": 5639632, "flower": "Pink and White Lady's Slipper"},
    "Mississippi": {"capital": "Jackson", "population": 2976149, "flower": "Magnolia"},
    "Missouri": {"capital": "Jefferson City", "population": 6137428, "flower": "Hawthorn"},
    "Montana": {"capital": "Helena", "population": 1068778, "flower": "Bitterroot"},
    "Nebraska": {"capital": "Lincoln", "population": 1934408, "flower": "Goldenrod"},
    "Nevada": {"capital": "Carson City", "population": 3080156, "flower": "Sagebrush"},
    "New Hampshire": {"capital": "Concord", "population": 1359711, "flower": "Purple Lilac"},
    "New Jersey": {"capital": "Trenton", "population": 8882190, "flower": "Violet"},
    "New Mexico": {"capital": "Santa Fe", "population": 2096829, "flower": "Yucca Flower"},
    "New York": {"capital": "Albany", "population": 19453561, "flower": "Rose"},
    "North Carolina": {"capital": "Raleigh", "population": 10488084, "flower": "Dogwood"},
    "North Dakota": {"capital": "Bismarck", "population": 762062, "flower": "Wild Prairie Rose"},
    "Ohio": {"capital": "Columbus", "population": 11689100, "flower": "Carnation"},
    "Oklahoma": {"capital": "Oklahoma City", "population": 3956971, "flower": "Oklahoma Rose"},
    "Oregon": {"capital": "Salem", "population": 4217737, "flower": "Oregon Grape"},
    "Pennsylvania": {"capital": "Harrisburg", "population": 12801989, "flower": "Mountain Laurel"},
    "Rhode Island": {"capital": "Providence", "population": 1059361, "flower": "Violet"},
    "South Carolina": {"capital": "Columbia", "population": 5148714, "flower": "Yellow Jessamine"},
    "South Dakota": {"capital": "Pierre", "population": 884659, "flower": "Pasque Flower"},
    "Tennessee": {"capital": "Nashville", "population": 6833174, "flower": "Iris"},
    "Texas": {"capital": "Austin", "population": 28995881, "flower": "Bluebonnet"},
    "Utah": {"capital": "Salt Lake City", "population": 3205958, "flower": "Sego Lily"},
    "Vermont": {"capital": "Montpelier", "population": 623989, "flower": "Red Clover"},
    "Virginia": {"capital": "Richmond", "population": 8535519, "flower": "Dogwood"},
    "Washington": {"capital": "Olympia", "population": 7614893, "flower": "Coast Rhododendron"},
    "West Virginia": {"capital": "Charleston", "population": 1792147, "flower": "Rhododendron"},
    "Wisconsin": {"capital": "Madison", "population": 5822434, "flower": "Wood Violet"},
    "Wyoming": {"capital": "Cheyenne", "population": 578759, "flower": "Indian Paintbrush"}
}

def display_states():
    """Display all states in alphabetical order with capital, population, and flower."""
    print(f"{'State':<15}{'Capital':<15}{'Population':<15}{'Flower'}")
    for state in sorted(states_data.keys()):
        print(f"{state:<15}{states_data[state]['capital']:<15}{states_data[state]['population']:<15}{states_data[state]['flower']}")

def search_state(state_name):
    """Search for a specific state and display its details along with the state flower image."""
    state = states_data.get(state_name)
    if state:
        print(f"{state_name} - Capital: {state['capital']}, Population: {state['population']}, Flower: {state['flower']}")
        # Display the image of the state flower
        try:
            flower_image_path = f"flower_images/{state_name}.png"  # Ensure images are named after states
            img = Image.open(flower_image_path)
            img.show()
        except FileNotFoundError:
            print(f"Image for {state['flower']} not found.")
    else:
        print("State not found!")

def bar_chart_top_5():
    """Display a bar chart of the top 5 populated states."""
    top_5_states = sorted(states_data.items(), key=lambda x: x[1]['population'], reverse=True)[:5]
    states = [state[0] for state in top_5_states]
    populations = [state[1]['population'] for state in top_5_states]

    plt.bar(states, populations, color='skyblue')
    plt.xlabel('States')
    plt.ylabel('Population')
    plt.title('Top 5 Populated States')
    plt.show()

def update_population(state_name, new_population):
    """Update the population for a specific state."""
    if state_name in states_data:
        states_data[state_name]['population'] = new_population
        print(f"Updated {state_name}'s population to {new_population}.")
    else:
        print("State not found!")

def menu():
    """Main menu function."""
    print("Welcome to the U.S. State Information Application!")
    while True:
        print("\nMenu:")
        print("1. Display all U.S. States in Alphabetical order")
        print("2. Search for a specific state")
        print("3. Display a bar chart of the top 5 populated states")
        print("4. Update the population of a specific state")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_states()
        elif choice == "2":
            state_name = input("Enter the name of the state: ")
            search_state(state_name)
        elif choice == "3":
            bar_chart_top_5()
        elif choice == "4":
            state_name = input("Enter the name of the state: ")
            try:
                new_population = int(input("Enter the new population: "))
                update_population(state_name, new_population)
            except ValueError:
                print("Invalid input. Please enter a valid population number.")
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
