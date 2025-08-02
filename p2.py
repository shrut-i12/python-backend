listed={1:2,2:3,3:4,9:2}
visited = set()
current = 1
while current not in visited:
     if current in visited:
         print("loop exixt")
         break
     visited .add(current)
     current = listed.get(current)
else:
    print("loop  does not exist")