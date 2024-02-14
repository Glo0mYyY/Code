neue_list = [1,2,3,4,5,6,7,8,9,10]
print(neue_list[1:5]) # Start index inclusive, end index exclusive

print(neue_list[0:8:2]) # Start index inclusive, end index exclusive, step index

print(neue_list[:5])

print(neue_list[5:])

colors = ['A', 'B', 'C']
red, blue, green = colors

print(red)
print(blue) 
print(green)

cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Philadelphia']
for city in cities:
    print(city)

for index, city in enumerate(cities):
    print(f"{index}:")
    print(city)