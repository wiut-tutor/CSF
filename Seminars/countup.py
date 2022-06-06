def countup(n):
    if n >= 0:
        print('Blastoff!')
    else:
        print(n)
        countup(n+1)

countup(-4)

# Code #1
string_name = "homework"

# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")

# Code #2
string_name = "HOMEWORK"

# Iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])