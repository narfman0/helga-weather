from parse_requirements_not_suckily import parse_requirements
from setuptools import setup, find_packages
from helga_weather import __version__ as version


setup(
    name='helga-weather',
    version=version,
    description=('Display weather from openweathermap.org'),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Topic :: Communications :: Chat :: Internet Relay Chat',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Communications :: Chat :: Internet Relay Chat'],
    keywords='irc bot weather urbandictionary urban dictionary ud',
    author='Jon Robison',
    author_email='narfman0@gmail.com',
    url='https://github.com/narfman0/helga-weather',
    license='LICENSE',
    packages=find_packages(),
    include_package_data=True,
    py_modules=['helga_weather.plugin'],
    zip_safe=True,
    install_requires=parse_requirements(),
    test_suite='',
    entry_points=dict(
        helga_plugins=[
            'weather = helga_weather.plugin:weather',
        ],
    ),
)
