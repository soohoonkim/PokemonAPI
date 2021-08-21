import requests

pokemon = input("Please enter the name or number of Pokemon that you want to see (type exit to exit): ")
    
try:
    pokemon = int(pokemon)
except:
    pokemon = str(pokemon)
    pokemon = pokemon.lower()

#passing user input to HTTP request URL
url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

#sprite of the pokemon
# p_sprite = pokemon_json["sprites"]['front_default']

#request pokemon and get the json data
pokemon_req = requests.get(url)
pokemon_json = pokemon_req.json()

#just getting the name of the Pokemon (does capitalize work like this?)
p_name = pokemon_json["name"].capitalize()

#list of moves the pokemon can learn
# p_moves = pokemon_json["moves"]
# print(f"Here is a list of all the moves {p_name} is known to learn across all of the Pokemon games...")
# for i in p_moves:
#     print(i['move']['name'], end=", ")

#list of pokemon stats
# p_stats = pokemon_json["stats"]
# print(f"\nThis is a list of {p_name}'s base stats:")
# for i in p_stats:
#     print(f"{i['stat']['name']}:\t {i['base_stat']}")

#list of abilities
p_abilities = pokemon_json["abilities"]
# print(p_abilities)
print(f"This is a list of {p_name}'s abilities")
for i in p_abilities:
    print(f'{i["ability"]["name"]}')

#looping through all abilities and requesting each url
for i in p_abilities:
    abilities_url = i["ability"]["url"]
    abilities_req = requests.get(abilities_url)
    abilities_json = abilities_req.json()
    p_abilities_description = abilities_json["effect_entries"]
    #parsing and selecting English language
    for i in p_abilities_description:
        if i["language"]["name"] == "en":
            print(abilities_json["name"])
            print(i["effect"])

# for i in p_abilities_description:
#     # if i["language"] == "en":
#     print(i["effect"])

#using status_code to check the status of the API server
# req = requests.get('https://pokeapi.co/')
# print(req.status_code)
