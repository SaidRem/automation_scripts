"""
The script works in command line.
Takes one command line argument after the script name for key in DATA
and retrieves by the key the data in DATA dict and places the data to the clipboard.
""" 

import sys
import pyperclip

DATA = {'t1': 'data1', # replace 't' keys and 'data' by useful data
        't2': 'data2',
        't3': 'data3',
        't4': 'data4',
        't5': 'data5'}


def main():
    if len(sys.argv) < 2:
        print('Usage: paste.py [key] => copy data to clipboard')
        sys.exit()
    
    key = sys.argv[1]     # first command line arg is a key to access data
    
    if key in DATA:
        pyperclip.copy(DATA[key])
        print(f'Data for {key} copied to clipboard.')
    else:
        print(f'There is no key named {key}')


if __name__ == "__main__":
    main()