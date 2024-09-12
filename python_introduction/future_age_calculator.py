
current_age = input("How old are you? ")
if current_age.isdigit():
    current_age = int(current_age)  
    age = current_age + (2050 - 2024)  
    print("In 2050, you will be", age, "years old.")
else:
    print("Please enter a proper value.")