# List data type implementation
# List allows to store multiple values and allows to store diff data types

values = [10, 25, 10.5, "Kameswara"]

print(values[0])

# Last value of a List
var = values[-1]

print(var)

# Sub List of a main list

print(values[1:3])

# Insert new value to List

values.insert(3, "Kameswara")

print(values)

# Modify a value in List

values[1]="Radhika"

# Add a value at the end of the List
values.append(var)

print(values)

# Remove a value in List
del  values[0]

print(values)
