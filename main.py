"""
Создание покемона POST 
"""
import requests

URL= "https://api.pokemonbattle.me"
Header= {'Content-Type':'application/json','trainer_token':'5e5efd135b4378f7afb166c73a8f8c53'}

body= {
    "pokemon_id": "22144"
}

#respohse = requests.post(url=f'{URL}/v2/pokemons',json=body,headers=Header,timeout=5)

#print(f'статус код:{respohse.status_code}.сообщение:{respohse.text}')

#respohse=requests.put(url=f'{URL}/v2/pokemons',headers=Header,json=body)
#print(f'статус код:{respohse.status_code}.')

respohse=requests.post(url=f'{URL}/v2/trainers/add_pokeball',headers=Header,json=body)
print(f'статус код:{respohse.status_code}.')