file = open('test.txt')

# print(file.read())

# Read specific / few bytes

# print(file.read(2))

# Read a file Linewise
# print(file.readline())

# Print all lines using a loop
# line = file.readline()

# while line != "":
#   print(line)
#  line = file.readline()


allContnet=file.readlines()

print(allContnet)
for i in allContnet:
    print(i)

file.close()
