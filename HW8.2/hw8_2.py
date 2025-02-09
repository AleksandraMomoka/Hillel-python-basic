import string

def is_palindrome(text):
    cleaned_text = text.lower().replace(' ', '')

    for symbol in string.punctuation:
        if cleaned_text.find(symbol) != -1:
            cleaned_text = cleaned_text.replace(symbol, '')

    if cleaned_text == cleaned_text[::-1]:
        return True
    else:
        return False

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

