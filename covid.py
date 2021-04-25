


age = input("Are you a cigarette addict older than 75 years old? ")
chronic = input("Do you have a severe chronic disease?")
immune = input("Is your immune system too weak?")
risk = False

if age == "Yes":
    age = True
else:
    age=False

if chronic == "Yes":
    chronic = True
else:
    chronic=False

if immune == "Yes":
    immune = True
else:
    immune = False



if immune or age or chronic:
    risk =True

else:
    risk = False

if risk:
    print("You are in risky group")

else:
    print("You are not in risky group")
    
