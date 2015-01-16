"""
Example script of constant use in Python. Constants should always be
  capitalized to signify their significance. Because everything is an object
  in Python and nothing can really be set as private, using visual
  identifiers, such as capitalizing all letters in a name and starting function
  names with an underscore, are important to for script readability.

This script uses two constants, URL and STATE, and then prints out a string
  using these constants for a state's download url (not a real url and doesn't
  actually download anything).

"""

URL = 'https://www.statedata.com/'
STATE = 'MD'

print 'Downloading data from {}{}'.format(URL, STATE)
