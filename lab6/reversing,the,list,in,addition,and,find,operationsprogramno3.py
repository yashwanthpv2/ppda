def display_list(lst):
    print("Current List:", lst)

def insert_element(lst):
    element = input("Enter the element to insert: ")
    position = int(input("Enter the position to insert the element (0-based index): "))
    
    if position < 0 or position > len(lst):
        print("Invalid position!")
    else:
        lst.insert(position, element)
        print(f"Element '{element}' inserted at position {position}.")

def delete_element(lst):
    element = input("Enter the element to delete: ")
    if element in lst:
        lst.remove(element)
        print(f"Element '{element}' has been removed from the list.")
    else:
        print(f"Element '{element}' not found in the list.")

def find_element(lst):
    element = input("Enter the element to find: ")
    if element in lst:
        print(f"Element '{element}' is found at position {lst.index(element)}.")
    else:
        print(f"Element '{element}' not found in the list.")

def sort_list(lst):
    lst.sort()
    print("List sorted in ascending order.")

def reverse_list(lst):
    lst.reverse()
    print("List reversed.")

def perform_operations():
    lst = []
    while True:
        print("\nSelect an operation:")
        print("1. Display List")
        print("2. Insert Element")
        print("3. Delete Element")
        print("4. Find Element")
        print("5. Sort List")
        print("6. Reverse List")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            display_list(lst)
        elif choice == '2':
            insert_element(lst)
        elif choice == '3':
            delete_element(lst)
        elif choice == '4':
            find_element(lst)
        elif choice == '5':
            sort_list(lst)
        elif choice == '6':
            reverse_list(lst)
        elif choice == '7':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice! Please select a valid option.")

# Start the program
perform_operations()
