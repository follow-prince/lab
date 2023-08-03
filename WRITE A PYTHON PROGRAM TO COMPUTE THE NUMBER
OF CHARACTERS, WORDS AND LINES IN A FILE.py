def count_chars_words_lines(file_name):
    try:
        with open(file_name, 'r') as file:
            data = file.read()
            num_chars = len(data)
            num_words = len(data.split())
            num_lines = data.count('\n') + 1
            return num_chars, num_words, num_lines
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return 0, 0, 0

# Example usage
file_name = 'example.txt'
num_chars, num_words, num_lines = count_chars_words_lines(file_name)
print(f"Number of characters: {num_chars}")
print(f"Number of words: {num_words}")
print(f"Number of lines: {num_lines}")
