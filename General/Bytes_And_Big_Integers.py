# Given large integer
large_integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the integer to bytes
# We need to determine the number of bytes. Each character is typically represented by 1 byte (8 bits).
# We can use the `to_bytes` method, specifying the number of bytes needed.
num_bytes = (large_integer.bit_length() + 7) // 8  # Calculate the number of bytes needed
byte_array = large_integer.to_bytes(num_bytes, 'big')

# Decode the byte array to a string
decoded_message = byte_array.decode('utf-8', errors='ignore')  # Use 'ignore' to skip any invalid bytes

# Print the result
print("Decoded Message:", decoded_message)
