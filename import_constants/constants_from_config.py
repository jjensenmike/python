"""
An example script to load constants and configuration variables from a
  separate configuration file. This allows you to load Python objects instead
  of strings that have to be then converted to Python objects and are loaded
  in awkwardly.

This script imports the DatabaseConnection class from the configuraton file and
  prints out the HOST, PORT, and USERNAME. This is all demo data with a fake
  HOST and USERNAME and does not connect to anything.

"""

from config import DatabaseConnection

print 'Connecting to {}:{}'.format(DatabaseConnection.HOST,
                                   DatabaseConnection.PORT)
print 'Connecting user: {}'.format(DatabaseConnection.USERNAME)
