import requests

base_url = 'http://localhost/pokemons/' 

def get_pokemons():
    response = requests.get(base_url)
    return response.json()

def get_pokemon_by_id(id:str):
    response = requests.get(base_url + str(id))
    return response.json()

def post_pokemon(pokemon:dict):
    response = requests.post(base_url, json = pokemon)
    return response.json()

def put_pokemon(id:str, pokemon:dict):
    response = requests.put(base_url + str(id), json = pokemon)
    return response.json()

def delete_pokemon(id:str):
    response = requests.delete(base_url + str(id))
    return response.json()


pokemon = {
    "nome":"pikachu",
    "peso":"150",
    "ataque":"250",
    "defesa":"350",
    "velocidade":"450",
    "habilidade1":"voadora",
    "habilidade2":"mata-leao"
}

result = get_pokemon_by_id(6)
print(result)


    