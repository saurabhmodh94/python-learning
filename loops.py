# LOOPS

people = ['Saurabh', 'Rutvik', 'Shubham', 'Suvas']

# FOR LOOP
for person in people:
    print(person)
    
# Iterate by seq index
for i in range(len(people)):
    print(people[i])
    
for i in range(20,25):
    print(i)
    
# WHILE LOOP

count = 0
while count<=10:
    count += 1
    if count==5:
        continue
    elif count==8:
        break
    print(count)