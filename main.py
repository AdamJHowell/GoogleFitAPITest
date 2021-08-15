import requests
import json

"""
https://developers.google.com/fit/rest
For the Fitness REST API, the URI format is:
    https://www.googleapis.com/fitness/v1/resourcePath?parameters
    https://developers.google.com/fit/datatypes/health#blood_pressure
"""


def list_data_sources(payload):
    # define headers and URL
    api_key = api_key_json['accessToken']
    url = config_json['dataSourceUrl']

    # Add API key and format to the payload
    payload['accessToken'] = api_key
    payload['format'] = 'json'
    json_print(payload)

    return requests.get(url, params=payload)


def json_print(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)


if __name__ == '__main__':
    with open('config.json') as file:
        config_json = json.load(file)
    with open('apiKey.json') as file:
        api_key_json = json.load(file)
    # headers = {'user-agent': 'BigGuyWhoKills'}

    # payload = {'api_key': api_key, 'method': 'chart.gettopartists', 'format': 'json'}
    response = list_data_sources({'method': 'chart.gettopartists'})
    # print(response.status_code)
    # print(response.text)
    print("Response JSON:")
    json_print(response.json())
