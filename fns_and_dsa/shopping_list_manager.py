def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize the empty shopping list

    while True:
        display_menu()
        choice = input("Enter your choice: ")  # Get user input for the menu choice

        if choice == '1':
            # Add an item to the shopping list
            added_item = input("Insert the item that you want to add: ").strip()  # Strip whitespace
            shopping_list.append(added_item)
            print(f"'{added_item}' has been added to the shopping list.")

        elif choice == '2':
            # Remove an item from the shopping list
            removed_item = input("Insert the item name to be removed: ").strip()
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"'{removed_item}' has been removed from the shopping list.")
            else:
                print(f"'{removed_item}' is not in the shopping list.")

        elif choice == '3':
            # Display the current shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")

        elif choice == '4':
            # Exit the program
            print("Goodbye!")
            break

        else:
            # Handle invalid menu choices
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
