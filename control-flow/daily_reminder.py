task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
match priority:
    case "high":
        message = f"'{task}' is a high priority task."
    case "medium":
        message = f"📝 '{task}' is a medium priority task."
    case "low":
    message = f"'{task}' is a low priority task."
    case_:
        message = f"'{task}' (priority not recognized)."
        if time_bound == "yes":
            message += " that requires your immediate attention today!"
        else:
            reminder += " Plan it as soon as possible." 
            print(f"Reminder:{message}")