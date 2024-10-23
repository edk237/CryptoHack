import base64

hex_string = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf"
converted = bytes.fromhex(hex_string)

# Affichage de la chaîne hexadécimale
print("Hex String:", hex_string)

# Affichage des bytes convertis
print("Converted Bytes:", converted)

# Conversion des bytes en chaîne de caractères
decoded_string = base64.b64encode(converted)
print("Decoded String:", decoded_string)

