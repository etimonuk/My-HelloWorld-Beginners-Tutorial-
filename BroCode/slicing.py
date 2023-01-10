#slicing = create a substring by extracting elelments from another string
# [start:stop:step]
# name = "Etim Etetim Onuk"

# first_name = name[:4]
# middle_name = name[5:11]
# last_name = name[12:]
# funky_name = name[::3]
# reverse_name = name[::-1]

# print(reverse_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7, -4)
print(website1[slice])
print(website2[slice])
