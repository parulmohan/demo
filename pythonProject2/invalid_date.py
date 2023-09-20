from datetime import datetime

def check_invalid_date_format(date_string, date_format):
    try:
        datetime.strptime(date_string, date_format)
        return False  # The date format is valid
    except ValueError:
        return True  # The date format is invalid

# Test invalid date formats
invalid_date_formats = [
    ("2023-07-20", "%d/%m/%Y"),  # Expected format: DD/MM/YYYY
    ("20/07-2023", "%d/%m/%Y"),  # Missing separator between day and month
    ("2023/July/20", "%Y %B %d"),  # Incorrect month representation
    ("07-20-2023", "%d/%m/%Y"),  # Expected format: DD/MM/YYYY
    ("20.07.2023", "%d/%m/%Y"),  # Expected format: DD/MM/YYYY
]

for date_string, date_format in invalid_date_formats:
    if check_invalid_date_format(date_string, date_format):
        print(f"Invalid date format: {date_string} does not match {date_format}")
    else:
        print(f"Valid date format: {date_string} matches {date_format}")