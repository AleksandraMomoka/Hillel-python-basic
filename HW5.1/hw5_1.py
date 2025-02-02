import keyword
import string

user_text = input('Type your variable name: ')

text_valid = True

if user_text in keyword.kwlist:
    print('keyword.kwlist')
    text_valid = False

if user_text[0] in string.digits:
    print('string.digits')
    text_valid = False

if not user_text.islower() and user_text != '_':
    print('user_text.islower()')
    text_valid = False

for symbol in string.punctuation:
    if symbol == '_':
        continue

    if user_text.find(symbol) != -1:
        text_valid = False

if len(user_text) == user_text.count('_') > 1:
    text_valid = False

if user_text.find(' ') != -1:
    text_valid = False

print(text_valid)
