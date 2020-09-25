import requests
number_of_hero = int(input('Write number of heroes: '))
dict_of_hero_intelligence = {}
while number_of_hero != 0:
    def Hero(name) :
        ''' Find a hero and return his intelligence '''
        response = requests.get(f'https://superheroapi.com/api/2619421814940190/search/{name}')
        hero = response.json()
        dict_of_hero_intelligence[name] = int(hero['results'][0]['powerstats']['intelligence'])
        return hero['results'][0]['powerstats']['intelligence']

    print(Hero(input('Write name of hero: ')))
    number_of_hero -= 1
for k,v in dict_of_hero_intelligence.items():
    max_ = max(dict_of_hero_intelligence.values())
    if max_ == v:
        print(f'The {k} has the most intelligence {v}')

# you are welcome =) hulk, Captain America, Thanos