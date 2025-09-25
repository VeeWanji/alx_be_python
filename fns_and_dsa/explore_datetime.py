from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date


def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("%Y-%m-%d")) 
    return future_date 

if _name_ == "_main_":
    current date = display_current_datetime()
    days = int(input("Enter number of days to add to the current date: "))



