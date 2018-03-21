import trunofficial

owner = trunofficial.search('2024561111')
print(owner.name)

mobile = owner.phone
print(mobile.number)
print(mobile.countrycode)
print(mobile.carrier)

house = owner.address
print(house.city)
print(house.timezone)