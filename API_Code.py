import json
import requests

def get_energy_data(api_key):
    headers = {'Authorization': f'Bearer {api_key}'}
    url = 'https://api.energydata.com/v1/energy'
    response = requests.get(url, headers=headers)
    return json.loads(response.text)
