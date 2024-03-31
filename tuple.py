# accessing items in a tuple
county = ("Nairobi", "Mombasa","Lamu","Nakuru", "Machakos")
print(county[2])


# adding items in a tuple
a = (1, 2, 3)
b = a + (4,)
print(b)

# removing an item from a tuple
county = ("Nairobi", "Mombasa","Lamu","Nakuru", "Machakos")
cty = county[:2] + county[3:]
print(cty)
