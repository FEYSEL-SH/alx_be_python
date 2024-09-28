
def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = int(input("Enter your choice: "))  
        if type(choice) == int:
            continue
        else:
            print("inter only number")
            
        
        if choice == 1:
            addedItem = str(input("insert the item that you want to add"))
            shopping_list.append(addedItem)
            pass
        elif choice == 2:
            removed_item = str(input("Insert the item name to be removed: "))
            if removed_item in shopping_list:
                shopping_list.remove(removed_item)
                print(f"{removed_item} has been removed from the shopping list.")
            else:
                print(f"{removed_item} is not in the shopping list.")
            pass
        elif choice == 3:

            print(f"{shopping_list}")
            pass
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

