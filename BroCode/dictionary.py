# dictionary = A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China': 'Beijing',
            'Russia': 'Moscow'}

# print(capitals['Russia'])  # shows error if the key:value isn't there
print(capitals.get('Germanny'))  # shows 'None' if key:value isn't there
