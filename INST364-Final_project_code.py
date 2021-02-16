'''
Miranda Clay
INST364 Final Project
'''
'''
This simulation will walk the user through 5 different cybersecurity scenarios, each which varying costs for consequences
'''

import random #random library will leave the outcomes up to chance

print("             _                                        _ _               _                 _       _             ")
print("   ___ _   _| |__   ___ _ __ ___  ___  ___ _   _ _ __(_) |_ _   _   ___(_)_ __ ___  _   _| | __ _| |_ ___  _ __ ")
print("  / __| | | | '_ \ / _ \ '__/ __|/ _ \/ __| | | | '__| | __| | | | / __| | '_ ` _ \| | | | |/ _` | __/ _ \| '__|")
print(" | (__| |_| | |_) |  __/ |  \__ \  __/ (__| |_| | |  | | |_| |_| | \__ \ | | | | | | |_| | | (_| | || (_) | |   ")
print("  \___|\__, |_.__/ \___|_|  |___/\___|\___|\__,_|_|  |_|\__|\__, | |___/_|_| |_| |_|\__,_|_|\__,_|\__\___/|_|   ")
print("       |___/                                                |___/                                               ")

print(" ")       
print("You are the new cybersecurity hire at NoName Inc. This company stores large amounts of valuable customer data that is often sought out by hackers wishing to make a profit.")
print("Your boss informs you that you need to make sure the company doesn't lose too much money to hackers since money is tight this year. You will play through 5 scenarios.")
print("You start with $5000.")
print(" ")

input("Press enter to continue...")
print(" ")
#create variable to store money
money = 5000
#show_money will print out how much money is left at the end of each decision
def show_money():
    print("You have $" + str(money) + " left")
    print(" ")

#check_money will check to see if there is still money left at the end of each round. The game ends if it falls below 0
def check_money():
    if money < 0:
        print("Sorry, too much money was lost. You lose.")
        input("Press enter to exit.")
        exit()


#scenario 1 (equal predicted outcomes)
print("Scenario 1: An email promising to give the recipient a cash prize is sent around to other employees of the company, however it asks for the recipients credentials to receive the award.")
print("The chances of someone falling for the phishing attack is 50%. If the attack is successful, $800 will be lost.")
print("You can either 1: Spend $400 to prevent the potential attack or 2: Trust that the other employees know it's a scam")
print("Input 1 or 2")
decision1 = input("")

random_outcome = random.randint(1, 100)

#the attack occurs if random number is between 1-50
if random_outcome <= 50:
    if decision1 == '1':
        money -= 400
        print("You decide to take initiative and prevent the attack for $400. It is successful!")

    if decision1 == '2':
        money -= 800
        print("You decide not to prevent the attack and the attack occurs. You lose $900.")

#the attack does NOT occur if random number is between 51-100
if random_outcome > 50:
    if decision1 == '1':
        money -= 400
        print("You decide to take initiative and prevent the attack for $400, but the attack didn't occur.")

    if decision1 == '2':
        print("You decide not to prevent the attack and the attack was unsuccessful! You don't lose any money.")

check_money()
show_money()

#scenario 2 (predicted outcome favors option 1)
print("Scenario 2: An employee decides to install a program on a work computer that you don't recognize.")
print("The chance that it is malware is 40% and could potentially cause a loss of $1500.")
print("You can either 1: Spend $500 to prevent the potential attack or 2: Ignore it because it might be a harmless program.")
print("Input 1 or 2")
decision2 = input("")

#the attack occurs if random number is between 1-40
random_outcome = random.randint(1, 100)

if random_outcome <= 40:
    if decision2 == '1':
        money -= 500
        print("You took precaution to ensure malware doesn't corrupt your databases for $500, and it was successful!")

    if decision2 == '2':
        money -= 1500
        print("You decide that it's probably harmless, but it was actually malware. You lose $1500.")

#the attack doesn't occur if random number is between 41-100
if random_outcome > 40:
    if decision2 == '1':
        money -= 500
        print("You took precaution to ensure malware doesn't corrupt your databases for $500, but it didn't end up being malware.")

    if decision2 == '2':
        print("You decide that it's probably harmless, and it was!")

check_money()
show_money()

#scenario 3 (predicted outcome favors option 2)
print("You realize that the company is vulnerable for a DDoS attack after checking to see what the previous cybersecurity professional before you implemented.")
print("The chance of a DDoS attack in the near future is 25% and could potentially cause a loss of $2000.")
print("You can either 1: Spend $800 to prevent the potential attack or 2: Ignore the possibility of an attack.")
print("Input 1 or 2")
decision3 = input("")

#the attack occurs if random number is between 1-25
random_outcome = random.randint(1, 100)

if random_outcome <= 25:
    if decision3 == '1':
        money -= 800
        print("You took precaution to prevent a DDoS attack for $800, and it was successful!.")

    if decision3 == '2':
        money -= 2000
        print("You decide to ignore the possibility of an attack and one occurs. You lose $2000.")

#the attack doesn't occur if random number is between 26-100
if random_outcome > 25:
    if decision3 == '1':
        money -= 800
        print("You took precaution to prevent the attack for $800, but it didn't end up happening.")

    if decision3 == '2':
        print("You decide not to fix the vulnerabilities and the attack didn't occur!")

check_money()
show_money()

#scenario 4 (predicted outcome favors option 1)
print("Because you company uses databases, this means SQL is the primary programming language, meaning a SQL injection attack could occur.")
print("The chance of A SQL injection attack is 35% and could potentially cause a loss of $3000.")
print("You can either 1: Spend $900 to prevent the potential attack or 2: Ignore the possibility of an attack.")
print("Input 1 or 2")
decision4 = input("")

random_outcome = random.randint(1, 100)

#the attack occurs if random number is between 1-30
if random_outcome <= 35:
    if decision4 == '1':
        money -= 900
        print("You took precaution to prevent the attack for $900, and it was successful!.")

    if decision4 == '2':
        money -= 3000
        print("You decide to ignore the possibility of an attack and one occurs. You lose $3000.")

#the attack doesn't occur if random number is between 31-100
if random_outcome > 35:
    if decision4 == '1':
        money -= 900
        print("You took precaution to prevent the attack for $900, but it didn't end up happening.")

    if decision4 == '2':
        print("You decide not to fix the vulnerabilities and the attack didn't occur!")

check_money()
show_money()

#scenario 5 (predicted outcome favors option 2)
print("You get an email threatening to encrpyt all information in the company's database if you don't pay a fee.")
print("The fee is $2500 and there is a 10% chance that this email was real. If it's real you lose the rest of your money ($5000).")
print("You can either 1: Pay the $2500 just to be safe or 2: Ignore the email")
print("Input 1 or 2")
decision5 = input("")

random_outcome = random.randint(1, 100)
#the attack occurs if random number is between 1-10
if random_outcome <= 10:
    if decision5 == '1':
        money -= 2500
        print("You decided to pay the $2500, and it was worth it because it was a real attack!")

    if decision5 == '2':
        money -= 5000
        print("You decide to ignore the possibility of an attack and one occurs. You lose the rest of your money.")

#the attack doesn't occur if random number is between 11-100
if random_outcome > 10:
    if decision5 == '1':
        money -= 2500
        print("You decided to pay the $2500, but the threat didn't end up being real.")

    if decision5 == '2':
        print("You decide to ignore the email and not pay. The attack wasn't real!")

check_money()
show_money()

print("Congratulations! You finished the game with $" + str(money) + "! Your boss is happy with your work!")
input("Press enter to exit...")
exit()