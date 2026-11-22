import time
import json
import random
import threading

state_lock = threading.Lock()
is_alive = True
withdraw = 0
money_in_bank = 2000
money = 0
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

def random_dealer_inventory(dealers_inventory, drugs):
    if len(drugs) == 0:
        return dealers_inventory

    count = random.randint(1, len(drugs))
    chosen = random.sample(drugs, k=count)

    for drug in chosen:
        name = drug["name"] if isinstance(drug, dict) else drug
        dealers_inventory.append(name)

    return dealers_inventory

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
        list_drugs_dealer(drugs)
    elif option == "2":
        buy_drug()
    elif option == "3":
        steal_from_dealer(inventory, dealers_inventory)
    else:
        print("INVAILD OPTION")
        dealer()

def bank():
    global money, money_in_bank

    while True:
        print(
            f"\nYou currently have {format_money(money_in_bank)} in the bank "
            f"and {format_money(money)} in your wallet."
        )
        option = input("Would you like to withdraw, deposit, or exit? (W/D/E): ").strip().lower()

        if option in ("w", "withdraw"):
            if money_in_bank <= 0:
                print("You don't have any money in the bank.")
                continue

            raw = input("How much would you like to withdraw? ").strip()
            try:
                amount = int(raw)
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > money_in_bank:
                print("You don't have that much in the bank.")
            else:
                money_in_bank -= amount
                money += amount
                print(
                    f"Withdrew {format_money(amount)}. "
                    f"Wallet: {format_money(money)} | Bank: {format_money(money_in_bank)}"
                )

        elif option in ("d", "deposit"):
            if money <= 0:
                print("You don't have any money in your wallet to deposit.")
                continue

            raw = input("How much would you like to deposit? ").strip()
            try:
                amount = int(raw)
            except ValueError:
                print("Please enter a valid whole number.")
                continue

            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > money:
                print("You don't have that much in your wallet.")
            else:
                money -= amount
                money_in_bank += amount
                print(
                    f"Deposited {format_money(amount)}. "
                    f"Wallet: {format_money(money)} | Bank: {format_money(money_in_bank)}"
                )

        elif option in ("e", "exit", "back", ""):
            print("Leaving the bank.")
            menu()
            return

        else:
            print("Invalid option. Please enter W, D, or E.")

def drug_menu():
    if not inventory:
        print("Your inventory is empty.")
        menu()
        return

    print("=== Your Drugs ===")
    for idx, item in enumerate(inventory, start=1):
        drug_name = item["name"] if isinstance(item, dict) else item
        print(f"  {idx}) {drug_name}")

    while True:
        choice = input("Enter a drug name to use (or 'back' to return): ").strip()
        if choice.lower() in ("back", "cancel", ""):
            menu()
            return

        for idx, item in enumerate(inventory):
            drug_name = item["name"] if isinstance(item, dict) else item
            if choice.lower() == drug_name.lower():
                used_item = inventory.pop(idx)
                print(f"You used {drug_name}!")
                # RESET WITHDRAW
                menu()
                return

        print("You don't have that drug in your inventory. Try again.")

def info():
    print("INFO")

def buy_drug():
    global money

    list_drugs(drugs)
    while True:
        option = input("Please enter Drug Name (or 'cancel' to go back): ").strip()
        if option.lower() in ("cancel", "back"):
            print("Cancelled.")
            return

        for drug in drugs:
            if option.lower() == drug["name"].lower():
                drug_name = drug["name"]
                price = drug["cost"]

                while True:
                    confirm = input(
                        f"Are you sure you want to buy {drug_name} for {format_money(price)}? (Y/N) "
                    ).strip().lower()

                    if confirm in ("yes", "y", ""):
                        if money >= price:
                            money -= price
                            inventory.append(drug_name)
                            print(f"Bought {drug_name}! You now have {format_money(money)} remaining.")
                            menu()
                        else:
                            print("YOU DO NOT HAVE THE FUNDS U BROKE PERSON")
                        return
                    elif confirm in ("no", "n"):
                        print("OK")
                        menu()
                        return
                    else:
                        print("Invalid Option. Please enter Y or N.")

        print("Drug not found. Try again.")

def format_money(money):
    return f"${money}"

def list_drugs(drug_list):
    print("=== For Sale ===")
    for drug in drug_list:
        name = f"=== {drug["name"]}, Price: {drug["cost"]} ==="
        print(name)

def list_drugs_dealer(drug_list):
    print("=== For Sale ===")
    for drug in drug_list:
        name = f"=== {drug["name"]}, Price: {drug["cost"]} ==="
        print(name)

    dealer()

def steal_from_dealer(inventory, dealers_inventory, success_chance=1):
    global dealers_name
    global is_alive

    if not dealers_inventory:
        print("they got nothing u stole all of it")
        menu()
        return False

    if random.random() < success_chance:
        
        item = dealers_inventory.pop(0)
        inventory.append(item)
        print(f"You got {inventory[-1]}")
        menu()
        return True
    else:
        print("The Dealer caught you pickpocketing and killed you.")
        is_alive = False
        return False

    dealers_name = get_random_dealer()

def main():
    random_dealer_inventory(dealers_inventory, drugs)
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