def inverter_string(s):
    string_invertida = ""
    for char in s:
        string_invertida = char + string_invertida
    return string_invertida

string = "Exemplo"
print(f"String original: {string}")
print(f"String invertida: {inverter_string(string)}")