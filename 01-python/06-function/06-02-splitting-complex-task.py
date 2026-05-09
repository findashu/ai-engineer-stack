# Splitting the complex task
# You are creating monthly report for an restaurant sales.
# Instead of putting all logic in one place, break it down
# Task
# Write function generate_report() that calls:
    # fetch_sales()
    # filter_valid_orders()
    # summarize_data()

def fetch_sales():
    print(f"Fetching sales")

def filter_valid_order():
    print(f"Filtering valid order")

def summarize_data():
    print(f"Summarizing the data")

def generate_report():
    fetch_sales()
    filter_valid_order()
    summarize_data()
    print(f"Report is ready!")

generate_report()