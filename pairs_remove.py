monkey = ["johnny", "mary", "sam"]

for x in monkey:
    monkey.remove(x)
    for y in monkey:
        if x != y:
           print(x + " " + y) 
        
