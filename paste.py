"""
The script works in command line.
Usage:
>> paste.py save <keyword>  # => saves clipboard to keyword.
>> paste.py <keyword>       # => loads from database by the <keyword> to clipboard.
>> paste allkeys            # => loads all keyword to clipboard.
""" 

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
            if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
                storage[sys.argv[2]] = pyperclip.paste()
            elif len(sys.argv) == 2:
                if sys.argv[1].lower() == 'allkeys':
                    pyperclip.copy(str(list(storage.keys())))
                elif sys.argv[1] in storage:
                    pyperclip.copy(storage[sys.argv[1]])
                else:
                    pyperclip.copy('Not such key')
    else:
        print('''Usage:
        paste.py save <keyword>   => saves clipboard to keyword.
        paste.py      <keyword>   => loads from database by the <keyword> to clipboard.
        paste         allkeys     => loads all keyword to clipboard.
        ''')


if __name__ == "__main__":
    copy_paste()
