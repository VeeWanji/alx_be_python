task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
while priority not in ["high", "medium", "low"]:
    print("Invalid priority! Please enter high, medium, or low.")
    priority = input("Priority (high/medium/low): ").lower()
match priority:
    case "high":
        reminder = f"⚡ '{task}' is a HIGH priority task."
        if time_bound == "yes":
            reminder += " 🚨 It requires your immediate attention today!"
        else:
            reminder += " Plan it as soon as possible to avoid delays."
    case "medium":
        reminder = f"📝 '{task}' is a MEDIUM priority task."
        if time_bound == "yes":
            reminder += " ⏰ Try to complete it today to stay on track."
        else:
            reminder += " Work on it when you have available time."
    case "low":
        reminder = f"☑️ '{task}' is a LOW priority task."
        if time_bound == "yes":
            reminder += " 🔔 Even though it's low priority, make time for it today."
        else:
            reminder += " Do it during your free time—no rush."
    case _:
        reminder = f"'{task}' has an unspecified priority. Decide when to complete it."
print("\nReminder:", reminder)
