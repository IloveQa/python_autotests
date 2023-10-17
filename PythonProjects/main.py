import requests

token = "58d2ba97f06175184ce621497a37605a"

response=requests.post('https://api.pokemonbattle.me:9104/pokemons',
     json={
    "name": "generate",
    "photo": "generate"},
    headers= {"Content-Type":"application/json","trainer_token":token})
print(response.text)




response_rename=requests.put('https://api.pokemonbattle.me:9104/pokemons',
     json={
    "pokemon_id": "12638",
    "name": "Alice",
    "photo":"https://dolnikov.ru/pokemons/albums/053.png"},
    headers= {"Content-Type":"application/json","trainer_token":token})
print(response_rename.text)






response_catchpok=requests.post('https://api.pokemonbattle.me:9104//trainers/add_pokeball',
     json={
    "pokemon_id": "12638"},
    headers= {"Content-Type":"application/json","trainer_token":token})
print(response_catchpok.text)









 