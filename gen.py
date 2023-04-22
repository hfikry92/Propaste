import pyperclip
import re
def read_file(filename="template.txt"):
    text_file = open(filename, "r")
    data = text_file.read()
    text_file.close()
    return data

def get_keys(file_content):
    return re.findall( r'<(.*?)>', file_content)
    
def _replace_all_in_dictionary(my_dict,file_content):
    for key in my_dict.keys():
        file_content = file_content.replace(key, my_dict[key])
    return file_content

def replace_values(keys, file_content):
    my_dict = {}
    for key in keys:
        val = input(f'How do you want to replace {key}?')
        my_dict[f"<{key}>"]= val
    # print(my_dict)
    file_content = _replace_all_in_dictionary(my_dict,file_content)
    return file_content

file_content = read_file()
keys_to_replace = get_keys(file_content)
new_value = replace_values(keys_to_replace,file_content)
pyperclip.copy(new_value)
