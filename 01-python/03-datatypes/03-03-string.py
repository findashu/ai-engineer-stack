# Strings are Immutable sequences of characters, used to represent text data. They can be defined using single quotes (' '), double quotes (" "), or triple quotes (''' ''' or """ """) for multi-line strings.

chai_type = "Normal Chai"
customer_name = 'John Doe'
print(f"Order for {customer_name}: {chai_type} please!")

chai_description = "Aromatic and Bold"

#Indexing
# Strings are indexed starting from 0. You can access individual characters using their index.
first_char = chai_description[0]
print(f"First character of description: {first_char}")

# Slicing
# You can extract a substring using slicing. The syntax is string[start:end:step], where start is the index to start from (inclusive) and end is the index to end at (exclusive).
substring = chai_description[0:9]
print(f"Sliced substring: {substring}")
print(f"Skipping characters: {chai_description[0:9:2]}")  # Skips every second character

#Reversing a string using slicing
reversed_description = chai_description[::-1]
print(f"Reversed description: {reversed_description}")


lable_text = "Chai Special"

ecoded_label = lable_text.encode('utf-8')
print(f"Encoded label (bytes): {ecoded_label}") 
decoded_label = ecoded_label.decode('utf-8')
print(f"Decoded label (string): {decoded_label}")