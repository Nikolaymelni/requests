def hero_iq(heroes, link):
    iq = 0
    smartest_hero = list()
    for hero in heroes:
        url = link + hero
        req = requests.get(url)
        hero_info = req.json()
        if int(hero_info['results'][0]['powerstats']['intelligence']) > iq:
            iq = int(hero_info['results'][0]['powerstats']['intelligence'])
            smartest_hero.clear()
            smartest_hero.append(hero_info['results'][0]['name'])
        elif int(hero_info['results'][0]['powerstats']['intelligence']) == iq:
            smartest_hero.append(hero_info['results'][0]['name'])

    return smartest_hero, iq

def main():
    heroes = ['Hulk', 'Captain America', 'Thanos']
    site = 'https://www.superheroapi.com/api/'
    api = '2619421814940190'
    link = site + api + '/search/'

    smartest_hero, iq = hero_iq(heroes, link)

    print(f"Самый высокий интеллект {iq}: ")
    for name in smartest_hero:
        print(name)


import requests
main()
