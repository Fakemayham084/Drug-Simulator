import time
import json
import random

withdraw = 0
money = 2000
age = 0
name = None
dealers_name = None
inventory = []
dealers_inventory = []

with open("names.json", "r") as f:
    people = json.load(f)

first = random.choice(people)["first_name"]
last = random.choice(people)["last_name"]

def get_random_dealer():
    dealer_first = random.choice(people)["first_name"]
    dealers_last = random.choice(people)["last_name"]
    return f"{dealer_first} {dealers_last}"

name = f"{first} {last}"
dealers_name = get_random_dealer()

drugs = [
    {"name": "Unicorn Rainbow", "cost": 200},
    {"name": "Pixie Dust", "cost": 600},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999}
]

def dealer():
    print("""===============================
=== PLEASE SELECT AN OPTION ===
===============================
  1) LIST DRUGS
  2) BUY DRUGS
  3) STEAL?
===============================""")  
    option = input()
    if option == "1":
        list_drugs(drugs)
    elif option == "2":
        buy_drug()
    elif option == "3":
        steal_from_dealer()
    else:
        print("INVAILD OPTION")

def bank():
    print("BANK")

def drug_menu():
    print("DRUG MENU")

def info():
    print("INFO")

def buy_drug():
    print("BUY")

def format_money(money):
    return f"${money}"

def list_drugs(drug_list):
    print("=== For Sale ===")
    for drug in drug_list:
        name = f"=== {drug["name"]}, Price: {drug["cost"]} ==="
        print(name)

    dealer()

def steal_from_dealer(inventory, dealers_inventory, success_chance=0.5):
    global dealers_name

    if not dealers_inventory:
        print("they got nothing u stole all of it")
        return False
        
    if random.random() < success_chance:
        print("PICKPOCKET GOOD")
        item = dealers_inventory.pop(0)
        inventory.append(item)
    else:
        print("PICKPOCKET BAD U DEAD")

    dealers_name = get_random_dealer()

def main():
    print(f"Welcome to drug simulator!\nYou start off with $2000\nand need to be on a drugs before the last one weres off and you go into withdraw.\nyou are also {name}\nthe game starts in 3 seconds\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    menu()

def menu():
    print("""===============================
=== PLEASE SELECT AN OPTION ===
===============================
  1) DEALER
  2) BANK
  3) DRUGS
  4) INFO
===============================""")  
    option = input("")
    if option == "1":
        dealer()
    elif option == "2":
        bank()
    elif option == "3":
        drug_menu()
    elif option == "4":
        info()
    else:
        print("INVAILD OPTION");
        menu()

main()