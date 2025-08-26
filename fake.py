# 1-random
import random

# 2-create subjects
subjects = [
    "Shahrukh Khan",
    "Virat Kohli",
    "Rahul Gandhi",
    "Mamata Banerje",
    "Salman Khan",
    "Alia Bhatt",
    "Sharadha Kapoor",
    "Rohit Sharma",
    "Orry",
    "A Group of Monkeys",
    "John Sina",
    "Rebel Kid",
    "Urfi Javed",
    "Sony Gandhi",
    "Honey Singh",
    "Badsha",
    "Darshan Raval",
    "Auto Rickshaw Driver from Delhi",
    "Boy from maharashtra",
    "Purav Jha",
    "Ananya Pandey",

]

actions = [
    "launches",
    "dances with",
    "makes fun with",
    "crys for",
    "laughs at",
    "eats",
    "drinks milk",
    "declares war on",
    "in bigboss",
    "orders",
    "sleeps on",
    "declares party",
    "throws party",
    "celebarates",
    "dies",
    " gave congratulations",
    "pushes",
    "jumps",
    "fights",
    "dive into",

]

place = [
    "inside parliament",
    "during IPL",
    "in hyderabad",
    "near marine drive",
    "nearby India Gate",
    "in railyway station",
    "in mumbai local train",
    "in Rajasthan fort",
    "in Mahabaleshvar",
    "during tour",
    "at Pushkar ghat",
    "a plate of samosa",
    "a plate of momo",
]

# 3 start the headline generation loop
while True:
    subject = random.choice(subjects)
    action = random.choice(actions)

    places = random.choice(place)

    headline = f" BREAKING NEWS: {subject} {action} {places}"
    print("\n" + headline + "\n")

    user_input = input("Do you want another headline? (yes/no)")
    if user_input.strip().lower() == "no":
        break


# print goodbye message
print("\nThanks for using the Fake News Headline Generator. Have a fun day and do visit again.")
