import requests

#simple program allowing a user to search for a pokemon using number or name from PokeAPI
while True:
    pokemon = input("Please enter the name or number of Pokemon that you want to see (type exit to exit): ")
    
    #exit option for the program
    if pokemon == "exit":
        break
    #checking if user entered ID or name of the Pokemon
    else:
        try:
            pokemon = int(pokemon)
        except:
            pokemon = str(pokemon)
            pokemon = pokemon.lower()

    #passing user input to HTTP request URL
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"

    #requesting, receiving json, parsing for "name", "ID", and "Type" and printing them for the requested pokemon all wrapped into a single function
    def get_pokemon():
        pokemon_req = requests.get(url)
        pokemon_json = pokemon_req.json()
        p_name = pokemon_json["name"]
        p_name = p_name.capitalize()
        p_id = pokemon_json["id"]
        p_type1 = pokemon_json["types"][0]["type"]["name"]
        try:
            p_type2 = pokemon_json["types"][1]["type"]["name"]
        except:
            p_type2 = None

        print(f'The Pokemon is {p_name}!')
        print(f"{p_name}'s Pokedex number is {p_id}.")
        if p_type2 is not None:
            print(f"{p_name} is a {p_type1} and {p_type2} type Pokemon.")
        else:
            print(f"{p_name} is a {p_type1} type Pokemon.")

    #customizing 2 separate error message depending on if the user entered ID or name...
    if type(pokemon) is int:
        try:
            get_pokemon()
        except Exception:
            print(f"You have entered pokemon number {pokemon}")
            print("This may be out of range...")
    else:
        try:
            get_pokemon()
        except Exception:
            print(f"You have entered {pokemon}...")
            print(f"{pokemon} is not a valid name of a pokemon...")
