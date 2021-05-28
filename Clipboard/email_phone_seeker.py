# The script finds phone number in clipboard text.
# All found phone numbers copy to the clipboard.

import pyperclip
import re

rus_phone_pat = re.compile(r'''(
                                ((\((\+7|8)\s?(\d{3})\))|  # area code with parentheses (+7 123)456-78-90
                                 ((\+7|8)\s?(\d{3}))|      # area code without parentheses (+7 123)456-78-90
                                 ((\+7|8)\s?\(\d{3}\))|    # area code without parentheses +7(123)456-78-90
                                 
                                )?    
                                (\s|-|\.)?
                                (\d{3})
                                (\s|-)?
                                (\d{2,3})
                                (\s|-)?
                                (\d{2,4})
                                )''', re.VERBOSE)

# emal regex
email_pat = re.compile(r'''(
                            [a-zA-Z0-9._%+-]+    # name
                            @                    # must have symbol
                            [a-zA-Z0-9.-]+       # domain name
                            (\.[a-zA-Z]{2,4})    # top-level domain name
                            )''', re.VERBOSE)    # 
# matches in clipboard text
text = str(pyperclip.paste())
results = []
for g in rus_phone_pat.findall(text):
    phone_num = g[0].replace('-', '')
    results.append(phone_num)

for g in email_pat.findall(text):
    results.append(g[0])

# join to string and copy result to clipboard
if results:
    pyperclip.copy('\n'.join(results))
    print('Results copied to clipboard: ')
    print('\n'.join(results))
else:
    print('There is no phone numbers or email found')