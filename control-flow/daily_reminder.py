task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()
match priority:
    case "high":
        reminder = f"⚡ '{task}' is a HIGH priority task."
    case "medium":
        reminder = f"📝 '{task}' is a MEDIUM priority task."
    case "low":
        reminder = f"☑️ '{task}' is a LOW priority task."
    case _:
        reminder = f"'{task}' has an unspecified priority."
if time_bound == "yes":
    if priority == "high":
        reminder += " 🚨 You must complete it immediately today!"
    elif priority == "medium":
        reminder += " ⏰ Try to finish it today to stay on track."
    else:  
        reminder += " 🔔 Even though it's low priority, schedule time today."
else:
    if priority == "high":
        reminder += " Plan it soon—don't let it slip!"
    elif priority == "medium":
        reminder += " Complete it when possible, but not urgent."
    else:
        reminder += " Do it in your free time, no rush."
print("\nReminder:", reminder)