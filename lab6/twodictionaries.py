def merge_dictionaries():
    """
    Merges two dictionaries entered by the user.
    """
    try:
        dict1_str = input("Enter the first dictionary (e.g., {'a': 1, 'b': 2}): ")
        dict1 = eval(dict1_str)  
        dict2_str = input("Enter the second dictionary (e.g., {'c': 3, 'd': 4}): ")
        dict2 = eval(dict2_str) 
        merged_dict = dict1.copy()  
        merged_dict.update(dict2)

        print("Merged dictionary:", merged_dict)

    except (SyntaxError, NameError, TypeError) as e:
        print("Invalid dictionary input. Please enter valid dictionaries in the specified format.")
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    merge_dictionaries()