def translate(text):
    result = []
    for char in text:
        if char.lower() in 'bcdfghjklmnpqrstvwxyz':
            result.append(char + 'o' + char.lower())
        else:
            result.append(char)
    return ''.join(result)

text = "this is fun"
print(translate(text))
