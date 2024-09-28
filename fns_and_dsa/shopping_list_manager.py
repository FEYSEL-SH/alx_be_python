def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))  # Ensuring input is an integer
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 4.")
            continue

        if choice == 1:
            added_item = input("Insert the item that you want to add: ").strip()
            shopping_list.append(added_item)
            print(f"'{added_item}' has been added to the shopping list.")
        
        elif choice == 2:
            removed_item = input("Insert the item name to be removed: ").strip()
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"'{removed_item}' has been removed from the shopping list.")
            else:
                print(f"'{removed_item}' is not in the shopping list.")
        
        elif choice == 3:
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
            print("Invalid choice. Please select a number between 1 and 4.")

if __name__ == "__main__":
    main()
