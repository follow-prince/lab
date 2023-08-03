import datetime

now = datetime.datetime.now()
print("Current date and time:")
print(now.strftime("%Y-%m-%d %H:%M:%S"))  # Output: 2023-08-03 12:34:56
print(now.strftime("%d/%m/%Y %H:%M:%S %p"))  # Output: 03/08/2023 12:34:56 AM
print(now.strftime("%a, %b %d, %Y"))  # Output: Thu, Aug 03, 2023
print(now.strftime("%c"))  # Output: Thu Aug  3 12:34:56 2023
  