from pakuri import *
from pakudex import *

def displayed_menu():
    # displaying menu and asking for which choice
    print("\nPakudex Main Menu")
    print("-----------------")
    print("1. List Pakuri\n2. Show Pakuri\n3. Add Pakuri")
    print("4. Evolve Pakuri\n5. Sort Pakuri\n6. Exit")

def main():
    #welcome message and prompt for capacity
    print("Welcome to Pakudex: Tracker Extraordinaire!")

    while True: #for the case where they include a non integer or a negative number for capacity
        try:
            max_cap = int(input("Enter max capacity of the Pakudex: "))
            if max_cap < 0:
                print("Please enter a valid size.")
            break
        except ValueError:
            print("Please enter a valid size.")

    pakudex = Pakudex(max_cap)
    print(f"The Pakudex can hold {max_cap} species of Pakuri.")

    while True: #this will always be true so menu will print
        displayed_menu()
        ask = input("What would you like to do?\n") #choose from 1-6

        #each choice and what happens
        if ask == "1":
            species_array = pakudex.get_species_array() #pakuri array is listed by index
            if species_array:
                print("Pakuri in Pakudex:")
                index = 1 #counts species
                for i in species_array:
                    print(f"{index}. {i}")
                    index += 1 #increment index for new place to print species
            else:
                print("No Pakuri in Pakudex yet!")
        elif ask == "2":  #stats printed for each respective index
            name = input("Enter the name of the species to display: ")
            statistics = pakudex.get_stats(name)
            if statistics:
                print(f"Species: {name}")
                print(f"Attack: {statistics[0]}")
                print(f"Defense: {statistics[1]}")
                print(f"Speed: {statistics[2]}")
            else:
                print(f"Error: No such Pakuri!")

        elif ask == "3": #adds each pakuri as long as it is not duplicated or capacity is full
            name = input("Enter the name of the species to add: ")
            if pakudex.add_pakuri(name):
                print(f"Pakuri species {name} successfully added!")
            else:
                print("Error: Pakudex already contains this species!")

        elif ask == "4": #evolves pakuri as long as it exists
            name = input("Enter the name of the species to evolve: ")
            if pakudex.evolve_species(name):
                print(f"{name} has evolved!")
            else:
                print("Error: No such Pakuri!")

        elif ask == "5": #sorts pakuri in order
            pakudex.sort_pakuri()
        elif ask == "6": #quits program
            print("Thanks for using Pakudex! Bye!")
            break
        else:
            print("Unrecognized menu selection!")


if __name__ == "__main__":
    main()

