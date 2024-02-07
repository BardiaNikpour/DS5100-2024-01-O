##Exersice 3.1



##Exercise 3.2
xx = [-2, 8, 0, 5, 6]
max_val = max(xx)
for x in xx:
    if x < max_val:
        print(x)

    else:
        print("max_val")


##Exercise 3.3
it = 0
max_iter = 100
while it < max_iter:
    if (it == 0) or (it % 10 == 0):
        print(it)
    it +=1


##Exercise 3.4
names = ["Audi", "BMW", "Honda", "Porsche"]
for name in names:
    print(name.lower())

##Exercise 3.5



##Exercise 3.6
 city = {
     "Sterling" : 20165,
     "Leesburg" : 20176
}
for city, zipcode in city.items():
    print(city, zipcode)
