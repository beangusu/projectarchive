def word_count(text):
    count = 0
    words = text.split()
    for word in words:
        count += 1
    print(f"Found {count} total words")

def char_count(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_chars(char_dict):
    sorted_list = []
    for char, count in char_dict.items():
        sorted_list.append({"char": char, "num": count})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(char):
    return char["num"]
