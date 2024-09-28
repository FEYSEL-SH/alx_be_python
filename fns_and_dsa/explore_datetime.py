import datetime
from datetime import timedelta
def display_current_datetime():
    current_date = datetime.datetime.now()

    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")
display_current_datetime()

def calculate_future_date():
    current_now = datetime.datetime.now()
    addDate = int(input("Enter the number of days to add to the current date:"))
    delta = timedelta(
    days=addDate,
)
    future_date = current_now + delta
    print(f"Future date: {future_date.strftime("%Y-%m-%d")}")
calculate_future_date()