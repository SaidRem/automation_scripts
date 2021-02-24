import pyperclip
import sys
import os

def splitter(text):
    if len(sys.argv) < 2:
        sep = input('Enter sign to separate: ').strip()
        result = text.split(sep)
        while result:
            pyperclip.copy(result[0])
            print('A part in the clipboard')
            result = result[1:]
            prom = input('More? (y/n) => ').strip()
            if prom != 'y':
                pyperclip.copy('')
                return
        pyperclip.copy('')
    
    elif len(sys.argv) == 2:
        sep = sys.argv[1]
        result = text.split(sep)
        while result:
            pyperclip.copy(result[0])
            print('A part of the text in the clipboard')
            result = result[1:]
            prom = input('More? (y/n) => ').strip()
            if prom != 'y':
                pyperclip.copy('')
                return
        pyperclip.copy('')


# TODO
# replace func



if __name__ == '__main__':
    text = pyperclip.paste()
    if text:
        splitter(text)

