import string


user_range = input('Type your range of letters: ')

alphabet = string.ascii_letters

start_index = alphabet.find(user_range[0])
end_index = alphabet.find(user_range[-1])
result = alphabet[start_index:end_index + 1]

print(result)
