def merge_dictionaries_with_addition(dict1, dict2):
    """
    Merges two dictionaries. If there are overlapping keys,
    the values are added in the merged dictionary.
    """
    merged_dict = dict1.copy()  
    for key, value in dict2.items():
        if key in merged_dict:
            if isinstance(merged_dict[key], (int, float)) and isinstance(value, (int, float)):
                merged_dict[key] += value
            elif isinstance(merged_dict[key], str) and isinstance(value, str):
                merged_dict[key] += value
            elif isinstance(merged_dict[key], list) and isinstance(value, list):
                merged_dict[key].extend(value)
            elif isinstance(merged_dict[key], tuple) and isinstance(value, tuple):
                merged_dict[key] += value
            else:
                print(f"Warning: Overlapping key '{key}' has values of incompatible types. Keeping value from the first dictionary.")
        else:
            merged_dict[key] = value

    return merged_dict

# Example usage:
dict_a = {'a': 10, 'b': 20, 'c': 30, 'd': [1, 2]}
dict_b = {'b': 5, 'c': 15, 'e': 40, 'd': [3, 4]}
dict_c = {'a': 'hello', 'f': 'world'}
dict_d = {'a': 'there', 'g': '!'}
dict_e = {'h': (1, 2), 'i': (3,)}
dict_f = {'h': (4,), 'j': 5}
dict_g = {'k': 10, 'l': 'text'}
dict_h = {'k': 'another', 'm': 20}

merged_ab = merge_dictionaries_with_addition(dict_a, dict_b)
print(f"Merged dict_a and dict_b: {merged_ab}")
merged_cd = merge_dictionaries_with_addition(dict_c, dict_d)
print(f"Merged dict_c and dict_d: {merged_cd}")
merged_ef = merge_dictionaries_with_addition(dict_e, dict_f)
print(f"Merged dict_e and dict_f: {merged_ef}")
merged_gh = merge_dictionaries_with_addition(dict_g, dict_h)
print(f"Merged dict_g and dict_h: {merged_gh}")