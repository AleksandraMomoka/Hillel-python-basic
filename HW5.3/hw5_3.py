import string


user_text = input('Type a text for hashtag: ')

start_hashtag = user_text.title().replace(' ','')

for symbol in string.punctuation:
    start_hashtag = start_hashtag.replace(symbol, '')

hashtag = '#' + start_hashtag[:139]

print(hashtag)
