import requests
import pytest

URL= "https://api.pokemonbattle.me"
Header= {'Content-Type':'application/json','trainer_token':'5e5efd135b4378f7afb166c73a8f8c53'}
def test_get_trainers():
    '''
     GET /trainers приходит с кодом 200 и имя твоего тренера
     '''
respohse = requests.get(url=f'{URL}/v2/trainers',params={'trainer_id': 2493},timeout=5)
assert respohse.status_code == 200,'Unexpected status code'