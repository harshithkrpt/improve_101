import time

# Current timestamp
# print(time.time())  # 1728360287.520236

# # Sleep for a bit (useful for pacing scripts)
# time.sleep(2)

# # Human-readable string
# print(time.ctime())  # Wed Oct  8 07:10:03 2025

# # Structured time object (like a named tuple)
# t = time.localtime()
# print(t.tm_year, t.tm_mon, t.tm_mday)

# # Format time manually
# formatted = time.strftime("%Y-%m-%d %H:%M:%S", t)
# print(formatted)  # 2025-10-08 07:10:03

from datetime import datetime, date, time, timedelta

# Current date and time
now = datetime.now()
print(now)  # 2025-10-08 07:10:03.512345

# Create specific date or time
d = date(2025, 10, 8)
t = time(14, 30, 0)

# Combine date and time
dt = datetime.combine(d, t)
print(dt)

# Add or subtract time
future = now + timedelta(days=7)
print(future)


# Parse and format
parsed = datetime.strptime("2025-10-08 14:30", "%Y-%m-%d %H:%M")
formatted = now.strftime("%A, %d %B %Y")
print(parsed, formatted)

import calendar

# Check leap year
print(calendar.isleap(2024))  # True

# Month calendar as a string
print(calendar.month(2025, 11))

# Get weekday (0 = Monday)
print(calendar.weekday(2025, 10, 8))  # 2 (Wednesday)

# Iterate over a month
for week in calendar.monthcalendar(2025, 10):
    print(week)
