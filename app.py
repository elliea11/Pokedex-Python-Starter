import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the entire pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def show_names():
    for pokemon in data:
        print(pokemon["name"]["english"])

# Add a language choice feature and print the pokemons name based on the user input
def language():
    print("Choose a language:")
    print("1 English")
    print("2 Japanese")
    print("3 Chinese")
    print("4 French")
x = int(input("Choose a language:"))
if x == 1:
    a
elif x == 2:
    b
elif x == 3:
    c
elif x == 4:
    d

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/flying, show all fire and flying moves. HINT import the moves.json file too!

