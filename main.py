import argparse
import os
import requests
from urllib.parse import urlparse
from dotenv import load_dotenv


BITLY_TOKEN = os.getenv('BITLY_TOKEN')
BASE_URL = 'https://api-ssl.bitly.com/v4'

def shorten_link(BITLY_TOKEN, user_input):
    address = '/shorten'
    full_url = f'{BASE_URL}{address}'
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    payload = {
        'long_url': user_input
    }
    response = requests.post(full_url, headers=headers, json=payload)
    response.raise_for_status()
    short_url = response.json()
    return short_url['link']

def count_clicks(BITLY_TOKEN, parsed_url):
    address = f'/bitlinks/{parsed_url}/clicks/summary'
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    parameters = {
        'unit': 'day', 
        'units' : '-1',
    }
    full_url = f'{BASE_URL}{address}'
    response = requests.get(full_url, headers=headers, params=parameters)
    response.raise_for_status()
    clicks_count = response.json()
    return clicks_count['total_clicks']

def cut_url_prefix(user_input):
    parse_url = urlparse(user_input)
    parsed_url = f'{parse_url.netloc}{parse_url.path}'
    return parsed_url

def check_for_bitlink(BITLY_TOKEN, parsed_url):
    address = f'/bitlinks/{parsed_url}'
    full_url = f'{BASE_URL}{address}'
    headers = {
        'Authorization': f'Bearer {BITLY_TOKEN}'
    }
    response = requests.get(full_url, headers=headers)
    return response.ok

def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('url', nargs='?')
    return parser

def main(bitly_token):
    parser = createParser()
    urlspace = parser.parse_args()
    if check_for_bitlink(bitly_token, cut_url_prefix(urlspace.url)):
        try:
            clicks_count = count_clicks(bitly_token, cut_url_prefix(urlspace.url))
            print('Кликов: ', clicks_count)
        except requests.exceptions.HTTPError as error:
            exit('Не могу получить данные о количестве кликов:\n{0}'.format(error))
    else:
        try:
            bitlink = shorten_link(bitly_token, urlspace.url)
            print('Битлинк: ', bitlink)
        except requests.exceptions.HTTPError as error:
            exit('Не могу получить данные с сервера:\n{0}'.format(error))

if __name__ == '__main__':
    load_dotenv()
    bitly_token = os.getenv('BITLY_TOKEN')
    main(bitly_token)
