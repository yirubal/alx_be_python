# daily_reminder.py

# Prompt for user inputs
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Match Case for priority levels
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"Note: '{task}' has an unrecognized priority level"

# Modify message if task is time-sensitive
if time_bound == "yes":
    reminder += " that requires immediate attention today!"
elif priority in ["low", "medium"]:
    reminder += ". Consider completing it when you have free time."

# Final reminder output
print("\n" + reminder)
