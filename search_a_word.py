# def search_word(filename, tar_word):
#     try:
#         with open(filename, 'r') as file:
#             lines = file.readlines()
#             words_in_lines = [line.split() for line in lines]
#             flat_list = [word for sublist in words_in_lines for word in sublist]
#             if tar_word.lower() in [word.lower() for word in flat_list]:
#                 print(f"{tar_word} appears in the {filename}")
#             else:
#                 print(f"{tar_word} not in the {filename}")
#     except FileNotFoundError:
#         print(f"File not exists")

def search_word(filename, word):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            nested_words_list = [line.split() for line in lines]
            words_list = []
            for ele in nested_words_list:
                if isinstance(ele, list):
                    words_list.extend(ele)
            if word in words_list:
                print(f"{word} exists in {filename}")
            else:
                print(f"{word} not exists in {filename}")

    except FileNotFoundError:
        print("File not exists")

search_word("examples.txt", "line")


search_word("examples.txt", "lines")