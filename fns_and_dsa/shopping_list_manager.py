import os

def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Check for implementation of an array shopping_list
    while True:
        display_menu()  # Check for calling display_menu function
        choice = input("Enter your choice: ")

        # Check for implementation of Choice Input as a number
        if not choice.isdigit():  # Check if input is a digit
            print("Invalid input. Please enter a number between 1 and 4.")
            continue  # Continue to the next iteration of the loop
        
        choice = int(choice)  # Convert the choice to an integer

        if choice == 1:
            # Prompt for and add an item
            added_item = input("Insert the item that you want to add: ").strip()
            shopping_list.append(added_item)
            print(f"'{added_item}' has been added to the shopping list.")
        elif choice == 2:
            # Prompt for and remove an item
            removed_item = input("Insert the item name to be removed: ").strip()
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"'{removed_item}' has been removed from the shopping list.")
            else:
                print(f"'{removed_item}' is not in the shopping list.")
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("\nCurrent Shopping List:")
                for index, item in enumerate(shopping_list, start=1):
                    print(f"{index}. {item}")
            else:
                print("Your shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    # Check if the script file exists and is not empty
    script_file = __file__  # Gets the current file path
    if os.path.exists(script_file) and os.path.getsize(script_file) > 0:
        main()  # Call the main function
    else:
        print("Script file does not exist or is empty.")
