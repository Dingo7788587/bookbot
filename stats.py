def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def count_char(text):
    return text["num"]

def chars_dict_to_sorted_list(chars_dict):
    chars_list = []
   
    for char, count in chars_dict.items():
        chars_list.append({"char": char, "num": count})
    
    chars_list.sort(reverse=True, key=count_char)
    
    return chars_list
