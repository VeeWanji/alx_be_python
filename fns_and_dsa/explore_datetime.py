from datetime import datetime, timedelta
def display_current_datetime():
    current_date = datetime.now()
    print("Current date and time:", current_date.strftime("YYYY-MM-DD HH:MM:SS"))
    return current_date


def calculate_future_date(current_date, days_to_add):
    future_date = current_date + timedelta(days=days_to_add)
    print("Future date:", future_date.strftime("YYYY-MM-DD))"))
    return future_date

if _name_ == "_main_":
    
