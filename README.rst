helga-weather
=============

.. image:: https://badge.fury.io/py/helga-weather.png
    :target: https://badge.fury.io/py/helga-weather

.. image:: https://travis-ci.org/narfman0/helga-weather.png?branch=master
    :target: https://travis-ci.org/narfman0/helga-weather

Display weather from openweathermap.org.

Usage
-----

`!weather <city>[,country code]`

Country code is an optional parameter, should be two characters

`!weather <lat=x&lon=y>`

Execute raw query against the given lat lon

Examples:

    !weather atlanta
    !weather london,uk
    !weather lat=35&lon=139

License
-------

Copyright (c) 2015 Jon Robison

See included LICENSE for licensing information
