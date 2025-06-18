a=[("Ali", 5), ("Zara", 4), ("Ali", 3),("Zara", 5)]
fakh={}
for i,fak in a:
    fakh.setdefault(i,[]).append(fak)
print(fakh)