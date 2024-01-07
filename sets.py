# Create an empty set
s = set()

# Add elements into the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)

s.remove(2)

print(s)
print(F"The set has {len(s)} elements")