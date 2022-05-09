import time
import requests


def questions(tag, fromdate, todate):
    site = 'https://api.stackexchange.com/2.3/questions'
    params = {'fromdate': fromdate, 'todate': todate, 'order': 'desc', 'sort': 'activity', 'tagged': tag,
              'site': 'stackoverflow'}
    response = requests.get(site, params=params)
    dict_json = response.json()
    print(f"Посты за последние 2 дня с тэгом - {tag}:\n")
    for question in dict_json['items']:
        print(f"- {question['title']}")
        print(question['link'], "\n")


current_time = int(time.time())
two_days = 172800
start_time = current_time - two_days
tag = 'Python'

questions(tag, start_time, current_time)
