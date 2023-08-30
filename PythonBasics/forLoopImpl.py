# For loop implentation

values = [10, 30, 40, 20, 50, 10]

for i in values:
    print(i * 2)

# Sum of first 5 Natural numbers

# range(x,y) means x to y-1 values

sum = 0
for j in range(1, 6):
    sum += j
print(sum)

# For loop with increment by 2 for every iteration
for k in range(1, 8, 2):
    print(k)
print("This iteration by 2 completed")


# For loop without initial index

for m in range(10):
    print(m)