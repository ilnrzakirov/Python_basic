import requests
import json

temp = dict()

data_on_deaths = json.loads(requests.get('https://breakingbadapi.com/api/deaths').text)
data_episode = json.loads(requests.get('https://breakingbadapi.com/api/episodes').text)
# TODO, к data_on_deaths стоит применить json.loads (десериализация объекта), и только после этого передать в функцию max.

max_deaths = max(data_on_deaths, key=lambda x: x['number_of_deaths'])

for episode in data_episode:
    if int(episode['episode']) == int(max_deaths['episode']):
        temp = episode
        break

result = dict()
result['season'] = temp['season']
result['episode'] = temp['episode']
result['number_of_deaths'] = max_deaths['number_of_deaths']
result['deceased_characters'] = temp['characters']
print(result)

with open('info.json', 'w') as file:
    json.dump(result, file, indent=4)