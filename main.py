import time

withdraw = 0
money = 2000
drugs = [
    {"name": "Unicorn Rainbow", "cost": 200},
    {"name": "Pixie Dust", "cost": 600},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999},
    {"name": "PLACEHOLDER", "cost": 999999}
]

def format_money(money):
    return f"${money}"

def list_drugs(drug_list):
    print("=== For Sale ===")
    for drug in drug_list:
        name = f"=== {drug["name"]}, Price: {drug["cost"]} ==="
        print(name)

def main():
    print("Welcome to drug simulator!\nYou start off with $2000\nand need to be on a drugs before the last one weres off and you go into withdraw.\nthe game starts in 3 seconds\n3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO")

def menu():
    pass
    
main()
list_drugs(drugs)
print(format_money(money))