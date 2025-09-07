
def get_num_words(text):
       words = text.split()
       return len(words)

def charcount(text):
    count = {}
    for char in text:
        i = char.lower()
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    return count


def helper_key(items):
     return items["num"]

def sorted_charcount(char_dict):
    list_dict = []
    for c, n in char_dict.items():
        if c.isalpha():
            list_dict.append({"char": c, "num": n})
        else:
            continue
    list_dict.sort(reverse=True, key=helper_key)
    return list_dict
    



    

    