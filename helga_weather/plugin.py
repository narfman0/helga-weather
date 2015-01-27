""" Plugin entry point for helga """
import json, requests
from helga.plugins import command
from helga import settings

_help_text = 'Display weather from openweathermap.org.\
Usage: !weather atlanta\
!weather london,uk'

@command('weather', help=_help_text)
def weather(client, channel, nick, message, cmd, args):
    """ Plugin entry point """
    if len(args) == 0:
        return u'You need to give me a city to look up.'
    locale = args[0]
    #check if we should use the default country code
    if ',' not in locale:
        country_code = getattr(settings, 'WEATHER_COUNTRY_CODE', 'us')
        locale += ',' + country_code
    locale = locale.capitalize()
    #execute and parse weather request
    try:
        data = execute_request(locale)
        temp_f, conditions = extract_weather(data)
        template = '{0} temp: {1}f conditions: {2}'
        return template.format(locale, temp_f, conditions)
    except Exception as e:
        return unicode('Weather exception for ' + locale + ":" + str(e))

def execute_request(locale):
    """ Invoke API to retrieve json hopefully representing request """
    api_url = 'http://api.openweathermap.org/data/2.5/weather?q='
    response = requests.get(api_url + locale)
    if response.status_code != 200:
        raise Exception('Status code returned: ' + str(response.status_code))
    response_json = json.loads(response.content)
    if not response_json:
        raise Exception('Response falsy for given locale: ' + locale)
    return response_json

def extract_weather(weather_json):
    """ Extract temperature and description """
    temp_kelvin = weather_json['main']['temp']
    temp_f = kelvin_to_fahrenheit(temp_kelvin)
    conditions = weather_json['weather'][0]['description']
    conditions = conditions.capitalize()
    return (temp_f, conditions)

def kelvin_to_fahrenheit(temp_kelvin):
    """ Convert kelvin temperatures to fahrenheit """
    return (temp_kelvin - 273.15) * 1.8 + 32
