"""
Example script to open and file using with/as. This handles file cleanup in
  background and provides a cleaner way to write file handling code.

This just opens 'ex.txt' and writes out the contents.

"""

with open('ex.txt', 'r') as r:
    print r.read()
