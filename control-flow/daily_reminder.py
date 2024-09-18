
def main():
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    match priority:
        case "high":
            reminder_message = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder_message += " that requires immediate attention today!"
            else:
                reminder_message += ". Consider completing it soon."
        case "medium":
            reminder_message = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                reminder_message += " that should be addressed soon!"
            else:
                reminder_message += ". You can schedule it for later."
        case "low":
            reminder_message = f"'{task}' is a low priority task"
            if time_bound == "yes":
                reminder_message += " but still needs to be done today!"
            else:
                reminder_message += ". Consider completing it when you have free time."
        case _:
            reminder_message = "Invalid priority level entered."
    print(f"Reminder: {reminder_message}")

if __name__ == "__main__":
    main()