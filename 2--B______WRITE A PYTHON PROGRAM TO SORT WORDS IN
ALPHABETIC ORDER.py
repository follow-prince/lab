words = input("Enter a list of words, separated by spaces: ").split()
words.sort()
print("The sorted list of words is:")
for word in words:
	print(word) 