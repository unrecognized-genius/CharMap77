encoding_map = {
    'А': '&2', 'Б': '√=', 'В': '[$', 'Г': 'π°', 'Д': '%™', 'Е': "-'", 'Ё': '_"', 'Ж': '©℅',
    'З': '÷=', 'И': '+-', 'Й': '#', 'К': '5(', 'Л': '13}', 'М': '99/{', 'Н': '61¢', 'О': '^•',
    'П': '~€', 'Р': '÷√', 'С': '©~', 'Т': '77^', 'У': '81)', 'Ф': '(|', 'Х': '¢π', 'Ц': '©¢$',
    'Ч': '12\\∆', 'Ш': '{√]', 'Щ': '&±', 'Ъ': '2&_', 'Ы': '_;', 'Ь': '3)', 'Э': '1℅°', 'Ю': '+1^',
    'Я': '*-"', ' ': '÷~', '.': "°", ',': "`", '*': "÷¥"
}

decoding_map = {v: k for k, v in encoding_map.items()}

def encode_text(text):
    result = []
    for char in text.upper():
        if char in encoding_map:
            result.append(encoding_map[char])
        else:
            result.append(char)
    return ''.join(result)

def decode_text(encoded_text):
    result = []
    temp = ''
    for char in encoded_text:
        temp += char
        if temp in decoding_map:
            result.append(decoding_map[temp])
            temp = ''
    return ''.join(result)

original_text = input("Введите слово: ")
encoded = encode_text(original_text)
decoded = decode_text(encoded)

print("\nОригинальный текст:", original_text)
print("\nЗакодированный текст:", encoded)
print("\nДекодированный текст:", decoded)
