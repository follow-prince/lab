n = 5

# Print upper half of the pattern
for i in range(n):
    for j in range(i):
        print('* ', end="")
    print('')

# Print lower half of the pattern
for i in range(n, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
