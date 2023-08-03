days_late = int(input("Enter the number of days late: "))

if days_late <= 0:
    print("Thank you for returning the book on time.")
elif days_late <= 5:
    fine = days_late * 0.5
    print(f"Fine: {fine:.2f} paisa")
elif days_late <= 10:
    fine = (5 * 0.5) + ((days_late - 5) * 1)
    print(f"Fine: {fine:.2f} rupees")
elif days_late <= 30:
    fine = (5 * 0.5) + (5 * 1) + ((days_late - 10) * 5)
    print(f"Fine: {fine:.2f} rupees")
else:
    print("Your membership has been cancelled for returning the book after 30 days.")
 