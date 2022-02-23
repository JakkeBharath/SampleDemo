#file=open("sample.txt")
#print(file.read())
#print(file.read(2))
#print(file.readline())
#print(file.readline())

#line=file.readline()
#while line!="":
    #print(line)
    #line=file.readline()
#print("file completed")
#for line in file.readlines():
 #   print(line)
#file.close()
with open('sample.txt', 'r') as reader:
    content = reader.readlines()
    reversed(content)
