age = int(input("Enter your age: "))

if age >= 18:
    print("ticket price is 10$ .")
elif age <= 18:
    print("ticket price is 5$ .")
elif age <= 13:
    print("ticket price is 1$ .")
elif age <= 5:
    print("ticket is free .")
