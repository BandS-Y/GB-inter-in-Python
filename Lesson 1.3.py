print("this is nedical anket")
user_name = input("enter your name: ")
user_age = int(input("enter your age: "))
user_mass = int(input("enter your mass: "))
if user_age <= 30 and (50 < user_mass  or user_mass < 120):
    print("all right")
elif 30 < user_age <= 40 and (50 > user_mass  or user_mass > 120):
    print("займитесь собой")
elif user_age > 40 and (50 > user_mass  or user_mass > 120):
    print("go to doctor")
else:
    print("Tребуется больше обследований")