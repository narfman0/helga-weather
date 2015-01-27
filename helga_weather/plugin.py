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
    query = args[0]
    #first check if this is an advanced query
    if '&' not in query:
        #naively assume it must be a simple city query
        #check if we should append default country code (not for lat/lon)
        if ',' not in query:
            country_code = getattr(settings, 'WEATHER_COUNTRY_CODE', 'us')
            query += ',' + country_code
        query = 'q=' + query.capitalize()
    #add default units if not explicit
    if 'units' not in query:
        query += '&units=' + getattr(settings, 'WEATHER_UNITS', 'imperial')
    #execute and parse weather request
    try:
        data = execute_request(query)
        temp_f, conditions = extract_weather(data)
        template = '{0} temp: {1}f conditions: {2}'
        return template.format(args[0], temp_f, conditions)
    except Exception as e:
        return unicode('Weather exception for ' + query + ":" + str(e))

def execute_request(query):
    """ Invoke API to retrieve json hopefully representing request """
    api_url = 'http://api.openweathermap.org/data/2.5/weather?'
    response = requests.get(api_url + query)
    if response.status_code != 200:
        raise Exception('Status code returned: ' + str(response.status_code))
    response_json = json.loads(response.content)
    if not response_json:
        raise Exception('Response falsy for given query: ' + query)
    return response_json

def extract_weather(weather_json):
    """ Extract temperature and description """
    temp_f = weather_json['main']['temp']
    conditions = weather_json['weather'][0]['description']
    conditions = conditions.capitalize()
    return (temp_f, conditions)
