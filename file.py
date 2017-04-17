# Open a file

fo=open('test.txt','w')

print(fo.name)
print(fo.closed)
print(fo.mode)

fo.write("I love python")
fo.write(" and JS")
fo.close()

fo=open('test.txt','a+')
fo.write("\nAlso React")
fo.close()

fo=open('test.txt','r+')
data=fo.read(6)
print(data)
fo.close()

fo=open("test2.txt",'w+')
fo.write("New File Test")
fo.close()