import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the entire pokedex list
data = json.load(pokedex)
print(data[0])

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.
def show_names(x):
    for pokemon in data:
        print(pokemon["name"][language])

# Add a language choice feature and print the pokemons name based on the user input
print("Choose a language:")
print("1 English")
print("2 Japanese")
print("3 Chinese")
x = int(input("Choose a language:"))
language = ""
if x == 1:
    language = "english"
elif x == 2:
    language = "japanese"
elif x == 3:
    language = "chinese"
show_names(language)

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user
types = []

for pokemon in data:
    for pokemon_type in pokemon["type"]:
        if pokemon_type not in types:
            types.append(pokemon_type)

print("Pokemon types:")
for pokemon_type in types:
    print(pokemon_type)

choice = input("Enter a Pokemon type: ").strip().lower()
found = False

for pokemon in data:
    for pokemon_type in pokemon["type"]:
        if pokemon_type.lower() == choice:
            print(pokemon["name"]["english"])
            found = True
            break

if found == False:
    print("No Pokemon were found with that type.")


#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


search = input("Enter a Pokemon's name: ").strip().lower()
found = False

if search == "":
    print("Please enter a name.")
        

for pokemon in data:
    name = pokemon["name"]["english"]

    if search in name.lower():
        print(name)
        found = True

if found == False:
    print("No Pokemon matched that name.")


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/flying, show all fire and flying moves. HINT import the moves.json file too!

