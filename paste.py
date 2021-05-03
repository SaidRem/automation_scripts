
# The script works in command line.

USAGE = '''Usage:
    paste.py save     <keyword>   => saves clipboard to keyword.
    paste.py <keyword>            => loads from database by the <keyword> to clipboard.
    paste.py allkeys              => loads all keyword to clipboard.
    paste.py del      <keyword>   => del data in the storage.
'''

import sys
import pyperclip
import shelve
import os

def copy_paste(direct=os.path.curdir):
    """
    Paste and copy to and from clipboard.
    direct - optional, path to storage dir.
    """
    storage_dir = os.path.abspath(direct)
    if len(sys.argv) > 1:
        with shelve.open(os.path.join(storage_dir, 'clipboard_storage')) as storage:
            if len(sys.argv) == 3: 
                if sys.argv[1].lower() == 'save':
                    storage[sys.argv[2]] = pyperclip.paste()
                elif sys.argv[1].lower() == 'del' and sys.argv[2] in storage:
                    del storage[sys.argv[2]]
            elif len(sys.argv) == 2:
                if sys.argv[1].lower() == 'allkeys':
                    pyperclip.copy(str(list(storage.keys())))
                elif sys.argv[1] in storage:
                    pyperclip.copy(storage[sys.argv[1]])
                else:
                    pyperclip.copy('Not such key')
            else:
                print(USAGE)
    else:
        print(USAGE)


if __name__ == "__main__":
    copy_paste()
