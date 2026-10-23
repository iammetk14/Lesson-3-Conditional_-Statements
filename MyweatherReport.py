city=input("Enter Your City name:")
temperature=float(input("Enter the temperature in your city:"))
if temperature>36:
    print("Warning: Very Hot! Stay Hydrated.")

if temperature>25:
    print("Pleasant weather! Nice day to go out.")
else:
    print("Pretty cold outside!")

if temperature>35:
    print("It is Very Hot. Be Careful and Stay Hydrated.")
elif temperature>25:
    print("The weather is quite pleasant. You may go out if you want but be careful and keep drinking water.")
elif temperature>15:
    print("The weather is quite cold. Wear atleast 2 layers of clothes if needed.")
else:
    print("The weather is EXTREMELY cold. Be careful and wear woolen clothes if going outside, with and jacket and hot water.")
import datetime
import calendar
now=datetime.datetime.now()
print("City:", city)
print("Current day, date and time:", now)
print(calendar.calendar(2026))