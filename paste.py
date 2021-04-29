"""
The script works in command line.

""" 

import sys
import pyperclip
import shelve

def main():
    with shelve.open('clipboard_storage') as storage:
        if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
            storage[sys.argv[2]] = pyperclip.paste()
        elif len(sys.argv) == 2:
            if sys.argv[1].lower() == 'list':
                pyperclip.copy(str(list(storage.keys())))
            elif sys.argv[1] in storage:
                pyperclip.copy(storage[sys.arg[1]])
            else:
                pyperclip.copy('Not such key')


if __name__ == "__main__":
    main()
