import requests

def get_smartest(heroes_list):
    url = "https://akabab.github.io/superhero-api/api/all.json"
    data = requests.get(url)
    smartest_hero_dict = {}
    for hero in data.json():
        for smartest_hero in heroes_list:
            if hero['name'] == smartest_hero:
                intelligence = hero['powerstats']['intelligence']
                smartest_hero_dict[smartest_hero] = intelligence
    return max(smartest_hero_dict, key=smartest_hero_dict.get)

print(f"����� ����� ����������: {get_smartest(['Hulk', 'Captain America', 'Thanos'])}")