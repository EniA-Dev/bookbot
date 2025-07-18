import re

def get_num_words(file_text):
    list_of_words = [word for word in re.split(' |\n', file_text) if word != ""]
    return len(list_of_words)

def character_counter(file_text):
    word_dict = {}
    for char in file_text:
        if word_dict.get(char.lower(), None) == None:
            word_dict[char.lower()] = 1
        else:
            word_dict[char.lower()] += 1
    return word_dict

def sorted_characters(file_text):
    counted_text = character_counter(file_text)
    def sort_on(items):
        return items["num"]
    
    expanded_dict = []
    for key,value in counted_text.items():
        if key.isalpha() == True:
            expanded_dict.append({"name":key,"num":value})
    expanded_dict.sort(reverse=True, key=sort_on)
    return expanded_dict
        