def count_words_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            word_count = sum(len(line.split()) for line in lines)

            print(f"Total number of lines: {line_count}")
            print(f"Total number of words: {word_count}")

    except FileNotFoundError:
        print("File not found, please check the file name or path")

count_words_lines("examples.txt")