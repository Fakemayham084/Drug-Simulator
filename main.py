import time
import random

is_alive = True
steal_chance = 1.0
warning_shown = False
withdrawal_time = None  # None until first drug is used
money_in_bank = 10000
money = 0
inventory = []
dealers_inventory = []

people = [
    {"id": 1, "first_name": "Teddi", "last_name": "Mucklestone"},
    {"id": 2, "first_name": "Ameline", "last_name": "Artharg"},
    {"id": 3, "first_name": "Eustace", "last_name": "Hurley"},
    {"id": 4, "first_name": "Konrad", "last_name": "Brockett"},
    {"id": 5, "first_name": "Chrysa", "last_name": "Zanardii"},
    {"id": 6, "first_name": "Clyve", "last_name": "Ruggen"},
    {"id": 7, "first_name": "Kaela", "last_name": "Paskell"},
    {"id": 8, "first_name": "Isaiah", "last_name": "Castard"},
    {"id": 9, "first_name": "Jaime", "last_name": "Bowles"},
    {"id": 10, "first_name": "Mitzi", "last_name": "Salmond"},
    {"id": 11, "first_name": "Boigie", "last_name": "Sliney"},
    {"id": 12, "first_name": "Devlen", "last_name": "Fountaine"},
    {"id": 13, "first_name": "Joseito", "last_name": "Gronowe"},
    {"id": 14, "first_name": "Godfry", "last_name": "Liston"},
    {"id": 15, "first_name": "Wyatan", "last_name": "Guilloud"},
    {"id": 16, "first_name": "Heda", "last_name": "Balding"},
    {"id": 17, "first_name": "Keith", "last_name": "Thaxton"},
    {"id": 18, "first_name": "Allen", "last_name": "Bickerdicke"},
    {"id": 19, "first_name": "Courtnay", "last_name": "Keller"},
    {"id": 20, "first_name": "Gabriello", "last_name": "Howey"},
    {"id": 21, "first_name": "Alberik", "last_name": "Sheriff"},
    {"id": 22, "first_name": "Xena", "last_name": "Brownell"},
    {"id": 23, "first_name": "Ludvig", "last_name": "McGreil"},
    {"id": 24, "first_name": "Staffard", "last_name": "Paz"},
    {"id": 25, "first_name": "Andrei", "last_name": "McGorman"},
    {"id": 26, "first_name": "Egan", "last_name": "Rawne"},
    {"id": 27, "first_name": "Appolonia", "last_name": "Driutti"},
    {"id": 28, "first_name": "Hieronymus", "last_name": "Nice"},
    {"id": 29, "first_name": "Guillema", "last_name": "Huxley"},
    {"id": 30, "first_name": "Lyell", "last_name": "Pinckney"},
    {"id": 31, "first_name": "Natalie", "last_name": "Theaker"},
    {"id": 32, "first_name": "Yolande", "last_name": "Kohn"},
    {"id": 33, "first_name": "Caleb", "last_name": "Kardos-Stowe"},
    {"id": 34, "first_name": "Dill", "last_name": "Domnin"},
    {"id": 35, "first_name": "Mandy", "last_name": "Tynan"},
    {"id": 36, "first_name": "Agnella", "last_name": "Ellson"},
    {"id": 37, "first_name": "Samson", "last_name": "Spieght"},
    {"id": 38, "first_name": "Thacher", "last_name": "Barendtsen"},
    {"id": 39, "first_name": "Gloria", "last_name": "Ofener"},
    {"id": 40, "first_name": "Son", "last_name": "Pockey"},
    {"id": 41, "first_name": "Andeee", "last_name": "Halburton"},
    {"id": 42, "first_name": "Roobbie", "last_name": "Medmore"},
    {"id": 43, "first_name": "Shellysheldon", "last_name": "Di Franceshci"},
    {"id": 44, "first_name": "Malanie", "last_name": "Dyde"},
    {"id": 45, "first_name": "Carmelina", "last_name": "McOrkill"},
    {"id": 46, "first_name": "Darb", "last_name": "Jesse"},
    {"id": 47, "first_name": "Carlotta", "last_name": "Troughton"},
    {"id": 48, "first_name": "Perry", "last_name": "Mathivat"},
    {"id": 49, "first_name": "Hertha", "last_name": "Sasser"},
    {"id": 50, "first_name": "Leoine", "last_name": "Wardhaugh"},
    {"id": 51, "first_name": "Corbett", "last_name": "Monsey"},
    {"id": 52, "first_name": "Bliss", "last_name": "Clewett"},
    {"id": 53, "first_name": "Kariotta", "last_name": "Jolland"},
    {"id": 54, "first_name": "Felecia", "last_name": "Cosans"},
    {"id": 55, "first_name": "Cirillo", "last_name": "Pauli"},
    {"id": 56, "first_name": "Vittoria", "last_name": "Sambrook"},
    {"id": 57, "first_name": "Hermie", "last_name": "Legging"},
    {"id": 58, "first_name": "Ray", "last_name": "Medwell"},
    {"id": 59, "first_name": "Ki", "last_name": "Blague"},
    {"id": 60, "first_name": "Gleda", "last_name": "Eggleson"},
    {"id": 61, "first_name": "Dulcia", "last_name": "Paffett"},
    {"id": 62, "first_name": "Heather", "last_name": "Ouldred"},
    {"id": 63, "first_name": "Gilda", "last_name": "Dwelley"},
    {"id": 64, "first_name": "Sanderson", "last_name": "O'Heaney"},
    {"id": 65, "first_name": "Bourke", "last_name": "Loughan"},
    {"id": 66, "first_name": "Ryan", "last_name": "Stear"},
    {"id": 67, "first_name": "Rori", "last_name": "Jopling"},
    {"id": 68, "first_name": "Arly", "last_name": "Whiscard"},
    {"id": 69, "first_name": "Gerhardine", "last_name": "Haighton"},
    {"id": 70, "first_name": "Daisie", "last_name": "Floch"},
    {"id": 71, "first_name": "Monro", "last_name": "Shawcroft"},
    {"id": 72, "first_name": "Christean", "last_name": "Martinolli"},
    {"id": 73, "first_name": "Byram", "last_name": "Havock"},
    {"id": 74, "first_name": "Daphne", "last_name": "Locket"},
    {"id": 75, "first_name": "Morse", "last_name": "Benedidick"},
    {"id": 76, "first_name": "Glennie", "last_name": "Swinfen"},
    {"id": 77, "first_name": "Kaycee", "last_name": "Hammel"},
    {"id": 78, "first_name": "Karel", "last_name": "Collisson"},
    {"id": 79, "first_name": "Terrel", "last_name": "Klasing"},
    {"id": 80, "first_name": "Holli", "last_name": "Orneblow"},
    {"id": 81, "first_name": "Tyler", "last_name": "Evesque"},
    {"id": 82, "first_name": "Archy", "last_name": "Heath"},
    {"id": 83, "first_name": "Anselma", "last_name": "Ruffey"},
    {"id": 84, "first_name": "Em", "last_name": "Mc Caghan"},
    {"id": 85, "first_name": "Scarlet", "last_name": "Vicar"},
    {"id": 86, "first_name": "Laurianne", "last_name": "Palatini"},
    {"id": 87, "first_name": "Edgar", "last_name": "Boerder"},
    {"id": 88, "first_name": "Bette-ann", "last_name": "Ogle"},
    {"id": 89, "first_name": "Libbie", "last_name": "Franceschielli"},
    {"id": 90, "first_name": "Osmond", "last_name": "Shubotham"},
    {"id": 91, "first_name": "Dinny", "last_name": "Farrah"},
    {"id": 92, "first_name": "Shaun", "last_name": "Scrammage"},
    {"id": 93, "first_name": "Pennie", "last_name": "Bowbrick"},
    {"id": 94, "first_name": "Lilian", "last_name": "Alabone"},
    {"id": 95, "first_name": "Marcelo", "last_name": "Walklot"},
    {"id": 96, "first_name": "Gabbi", "last_name": "Beaushaw"},
    {"id": 97, "first_name": "Maryjane", "last_name": "Pietrzyk"},
    {"id": 98, "first_name": "Hale", "last_name": "Freeborn"},
    {"id": 99, "first_name": "Reynold", "last_name": "Dupre"},
    {"id": 100, "first_name": "Gregorius", "last_name": "Klosges"},
    {"id": 101, "first_name": "Fleur", "last_name": "Toplin"},
    {"id": 102, "first_name": "Elisabet", "last_name": "Champley"},
    {"id": 103, "first_name": "Tomasina", "last_name": "Nowaczyk"},
    {"id": 104, "first_name": "Rosemonde", "last_name": "Pear"},
    {"id": 105, "first_name": "Paolo", "last_name": "MacIlhargy"},
    {"id": 106, "first_name": "Glynda", "last_name": "Bowmaker"},
    {"id": 107, "first_name": "Lisha", "last_name": "Dampier"},
    {"id": 108, "first_name": "Nathanial", "last_name": "Hatliff"},
    {"id": 109, "first_name": "Cele", "last_name": "Pfaffe"},
    {"id": 110, "first_name": "Tybalt", "last_name": "Gilham"},
    {"id": 111, "first_name": "Orly", "last_name": "Assiratti"},
    {"id": 112, "first_name": "Vaughan", "last_name": "Haborn"},
    {"id": 113, "first_name": "Adrianna", "last_name": "Gogay"},
    {"id": 114, "first_name": "Mannie", "last_name": "Lowdwell"},
    {"id": 115, "first_name": "Nickolaus", "last_name": "Huegett"},
    {"id": 116, "first_name": "Jethro", "last_name": "Brodeur"},
    {"id": 117, "first_name": "Margy", "last_name": "Burnie"},
    {"id": 118, "first_name": "Kelly", "last_name": "Carpenter"},
    {"id": 119, "first_name": "Fanny", "last_name": "Cruxton"},
    {"id": 120, "first_name": "Nico", "last_name": "Tolley"},
    {"id": 121, "first_name": "Ignazio", "last_name": "Rodrig"},
    {"id": 122, "first_name": "Teodora", "last_name": "Huddlestone"},
    {"id": 123, "first_name": "Bob", "last_name": "Coudray"},
    {"id": 124, "first_name": "Chen", "last_name": "Ozanne"},
    {"id": 125, "first_name": "Christine", "last_name": "Mallabon"},
    {"id": 126, "first_name": "Whitaker", "last_name": "Rosenzveig"},
    {"id": 127, "first_name": "Carny", "last_name": "Druery"},
    {"id": 128, "first_name": "Teirtza", "last_name": "Piddle"},
    {"id": 129, "first_name": "Pete", "last_name": "Noah"},
    {"id": 130, "first_name": "Marcelle", "last_name": "Jeram"},
    {"id": 131, "first_name": "Ola", "last_name": "Clawe"},
    {"id": 132, "first_name": "Bambi", "last_name": "Seston"},
    {"id": 133, "first_name": "Sharl", "last_name": "Goulborn"},
    {"id": 134, "first_name": "Saxe", "last_name": "Kubatsch"},
    {"id": 135, "first_name": "Pryce", "last_name": "Syphas"},
    {"id": 136, "first_name": "Tripp", "last_name": "Clows"},
    {"id": 137, "first_name": "Jsandye", "last_name": "Avramovic"},
    {"id": 138, "first_name": "Manny", "last_name": "Jodlowski"},
    {"id": 139, "first_name": "Debera", "last_name": "Frohock"},
    {"id": 140, "first_name": "Harwilll", "last_name": "Binnion"},
    {"id": 141, "first_name": "Matthias", "last_name": "Chaffer"},
    {"id": 142, "first_name": "Cristi", "last_name": "Minillo"},
    {"id": 143, "first_name": "Nina", "last_name": "Simoni"},
    {"id": 144, "first_name": "Otis", "last_name": "Esposi"},
    {"id": 145, "first_name": "Free", "last_name": "Coat"},
    {"id": 146, "first_name": "Kevin", "last_name": "Prantoni"},
    {"id": 147, "first_name": "Cassie", "last_name": "Ferretti"},
    {"id": 148, "first_name": "Francesco", "last_name": "Drury"},
    {"id": 149, "first_name": "Mathian", "last_name": "Waddington"},
    {"id": 150, "first_name": "Noll", "last_name": "Southgate"},
    {"id": 151, "first_name": "Murvyn", "last_name": "Steanyng"},
    {"id": 152, "first_name": "Ibbie", "last_name": "Roantree"},
    {"id": 153, "first_name": "Shaylyn", "last_name": "Jenteau"},
    {"id": 154, "first_name": "Skippie", "last_name": "Randlesome"},
    {"id": 155, "first_name": "Franny", "last_name": "Borless"},
    {"id": 156, "first_name": "Elsi", "last_name": "McKoy"},
    {"id": 157, "first_name": "Karel", "last_name": "Abbis"},
    {"id": 158, "first_name": "Kelbee", "last_name": "Saladin"},
    {"id": 159, "first_name": "King", "last_name": "Midlar"},
    {"id": 160, "first_name": "Eugen", "last_name": "Hawtin"},
    {"id": 161, "first_name": "Felizio", "last_name": "Barefoot"},
    {"id": 162, "first_name": "Roderic", "last_name": "Whitney"},
    {"id": 163, "first_name": "Ali", "last_name": "Peevor"},
    {"id": 164, "first_name": "Mendie", "last_name": "Stitfall"},
    {"id": 165, "first_name": "Marylou", "last_name": "Bisatt"},
    {"id": 166, "first_name": "Dael", "last_name": "Harnor"},
    {"id": 167, "first_name": "Duncan", "last_name": "Wisdish"},
    {"id": 168, "first_name": "Clemmie", "last_name": "Bartul"},
    {"id": 169, "first_name": "Keene", "last_name": "Roylance"},
    {"id": 170, "first_name": "Chanda", "last_name": "Crookshank"},
    {"id": 171, "first_name": "Helaina", "last_name": "Silwood"},
    {"id": 172, "first_name": "Thomasa", "last_name": "Swaile"},
    {"id": 173, "first_name": "Scot", "last_name": "Zealy"},
    {"id": 174, "first_name": "Nial", "last_name": "Pegg"},
    {"id": 175, "first_name": "Julissa", "last_name": "Korlat"},
    {"id": 176, "first_name": "Ardyth", "last_name": "Cartledge"},
    {"id": 177, "first_name": "Laureen", "last_name": "Scardefield"},
    {"id": 178, "first_name": "Gerry", "last_name": "Tubbles"},
    {"id": 179, "first_name": "Von", "last_name": "Shaw"},
    {"id": 180, "first_name": "Benson", "last_name": "Ezzy"},
    {"id": 181, "first_name": "Sara", "last_name": "Headings"},
    {"id": 182, "first_name": "Jenna", "last_name": "Dmitrienko"},
    {"id": 183, "first_name": "Lyle", "last_name": "Balstone"},
    {"id": 184, "first_name": "Noelyn", "last_name": "Gridley"},
    {"id": 185, "first_name": "Pace", "last_name": "Soldner"},
    {"id": 186, "first_name": "Krystal", "last_name": "Hairon"},
    {"id": 187, "first_name": "Lauren", "last_name": "Strain"},
    {"id": 188, "first_name": "Josepha", "last_name": "Delete"},
    {"id": 189, "first_name": "Valeda", "last_name": "Benedite"},
    {"id": 190, "first_name": "Sibella", "last_name": "Lowton"},
    {"id": 191, "first_name": "Nikkie", "last_name": "Stiller"},
    {"id": 192, "first_name": "Carmina", "last_name": "Stennings"},
    {"id": 193, "first_name": "Shirline", "last_name": "Traise"},
    {"id": 194, "first_name": "Tibold", "last_name": "Hlavac"},
    {"id": 195, "first_name": "Elie", "last_name": "Szantho"},
    {"id": 196, "first_name": "Lenka", "last_name": "Hamblen"},
    {"id": 197, "first_name": "Jami", "last_name": "Newiss"},
    {"id": 198, "first_name": "Bianka", "last_name": "Symmers"},
    {"id": 199, "first_name": "Maggee", "last_name": "Bodega"},
    {"id": 200, "first_name": "Sande", "last_name": "Carefull"},
    {"id": 201, "first_name": "Lynna", "last_name": "Mounter"},
    {"id": 202, "first_name": "Hillary", "last_name": "Henrionot"},
    {"id": 203, "first_name": "Linn", "last_name": "McIlvenna"},
    {"id": 204, "first_name": "Jessey", "last_name": "Ells"},
    {"id": 205, "first_name": "Carlos", "last_name": "Maypother"},
    {"id": 206, "first_name": "Zahara", "last_name": "Spear"},
    {"id": 207, "first_name": "Prescott", "last_name": "Farenden"},
    {"id": 208, "first_name": "Isak", "last_name": "Stephens"},
    {"id": 209, "first_name": "Raffaello", "last_name": "Boddie"},
    {"id": 210, "first_name": "Fonz", "last_name": "Vakhrushin"},
    {"id": 211, "first_name": "Aretha", "last_name": "Hobbema"},
    {"id": 212, "first_name": "Wandie", "last_name": "Merring"},
    {"id": 213, "first_name": "Clive", "last_name": "Dunbobin"},
    {"id": 214, "first_name": "Dorise", "last_name": "Desforges"},
    {"id": 215, "first_name": "Padget", "last_name": "Dymock"},
    {"id": 216, "first_name": "Reba", "last_name": "Biernacki"},
    {"id": 217, "first_name": "Ibrahim", "last_name": "Shanklin"},
    {"id": 218, "first_name": "Emmerich", "last_name": "Cherry"},
    {"id": 219, "first_name": "Mindy", "last_name": "McKevitt"},
    {"id": 220, "first_name": "Sheri", "last_name": "Ornelas"},
    {"id": 221, "first_name": "Vernice", "last_name": "Dranfield"},
    {"id": 222, "first_name": "Davina", "last_name": "Orriss"},
    {"id": 223, "first_name": "Aloise", "last_name": "Schindler"},
    {"id": 224, "first_name": "Donetta", "last_name": "Gravie"},
    {"id": 225, "first_name": "Mildred", "last_name": "Kopfen"},
    {"id": 226, "first_name": "Annabal", "last_name": "Sarjent"},
    {"id": 227, "first_name": "Hedi", "last_name": "Hargrave"},
    {"id": 228, "first_name": "Meagan", "last_name": "Sturridge"},
    {"id": 229, "first_name": "Corbie", "last_name": "Costelloe"},
    {"id": 230, "first_name": "Adair", "last_name": "Clem"},
    {"id": 231, "first_name": "Ashia", "last_name": "Neylan"},
    {"id": 232, "first_name": "Carmella", "last_name": "Leafe"},
    {"id": 233, "first_name": "Camile", "last_name": "Hunday"},
    {"id": 234, "first_name": "Bradford", "last_name": "Masham"},
    {"id": 235, "first_name": "Piotr", "last_name": "Maso"},
    {"id": 236, "first_name": "Zorine", "last_name": "Collard"},
    {"id": 237, "first_name": "Mallory", "last_name": "Burrell"},
    {"id": 238, "first_name": "Sari", "last_name": "Cuer"},
    {"id": 239, "first_name": "Wandis", "last_name": "Mogey"},
    {"id": 240, "first_name": "Rosanna", "last_name": "Jurczik"},
    {"id": 241, "first_name": "Bendite", "last_name": "Sweett"},
    {"id": 242, "first_name": "Nye", "last_name": "MacIan"},
    {"id": 243, "first_name": "Beatrix", "last_name": "Buscher"},
    {"id": 244, "first_name": "Tybie", "last_name": "Tuftin"},
    {"id": 245, "first_name": "Teodoro", "last_name": "Waterfield"},
    {"id": 246, "first_name": "Merrie", "last_name": "Overthrow"},
    {"id": 247, "first_name": "Barbe", "last_name": "Phippard"},
    {"id": 248, "first_name": "Phyllys", "last_name": "Kynaston"},
    {"id": 249, "first_name": "Byran", "last_name": "Verbruggen"},
    {"id": 250, "first_name": "Thelma", "last_name": "Chasemore"},
]

first = random.choice(people)["first_name"]
last = random.choice(people)["last_name"]
age = random.randint(20, 100)


def get_random_dealer():
    dealer_first = random.choice(people)["first_name"]
    dealers_last = random.choice(people)["last_name"]
    return f"{dealer_first} {dealers_last}"


name = f"{first} {last}"
dealers_name = get_random_dealer()

drugs = [
    {"name": "Unicorn Rainbow", "cost": 200, "withdraw_time": 20},
    {"name": "Pixie Dust", "cost": 600, "withdraw_time": 60},
    {"name": "Starlight Frost", "cost": 950, "withdraw_time": 80},
    {"name": "Velvet Eclipse", "cost": 1300, "withdraw_time": 100},
    {"name": "Solar Flare", "cost": 1650, "withdraw_time": 120},
    {"name": "Void Essence", "cost": 2000, "withdraw_time": 150},
]


def start_or_reset_withdrawal(seconds=20):
    global withdrawal_time, warning_shown
    withdrawal_time = time.monotonic() + seconds
    warning_shown = False


def stop_withdrawal():
    global withdrawal_time, warning_shown
    withdrawal_time = None
    warning_shown = False


def check_withdrawal():
    global is_alive, steal_chance, warning_shown

    if not is_alive or withdrawal_time is None:
        return True

    remaining = withdrawal_time - time.monotonic()

    if remaining <= 0:
        print("\nYou went into withdrawal and died!\nRIP")
        is_alive = False
        return False

    if remaining <= 5:
        steal_chance = 0.5
        if not warning_shown:
            print(f"\nWarning: Withdrawal in {int(remaining) + 1} seconds! Use a drug or u die")
            warning_shown = True
    elif remaining <= 10:
        steal_chance = 0.8
    else:
        steal_chance = 1.0

    return True


def random_dealer_inventory(dealers_inventory, drugs):
    if not drugs:
        return dealers_inventory

    count = random.randint(1, len(drugs))
    chosen = random.sample(drugs, k=count)

    for drug in chosen:
        drug_name = drug["name"] if isinstance(drug, dict) else drug
        dealers_inventory.append(drug_name)

    return dealers_inventory


def dealer():
    while is_alive:
        if not check_withdrawal():
            return

        print(f"""===============================
=== DEALER: {dealers_name} ===
===============================
  1) LIST DRUGS
  2) BUY DRUGS
  3) STEAL?
  4) BACK
===============================""")
        option = input("> ").strip()

        if not check_withdrawal():
            return

        if option == "1":
            list_drugs(drugs)
        elif option == "2":
            buy_drug()
        elif option == "3":
            steal_from_dealer(inventory, dealers_inventory, steal_chance)
        elif option in ("4", "back", ""):
            return
        else:
            print("INVALID OPTION")


def bank():
    global money, money_in_bank

    while is_alive:
        if not check_withdrawal():
            return

        print(
            f"\nYou currently have {format_money(money_in_bank)} in the bank "
            f"and {format_money(money)} in your wallet."
        )
        option = input("Would you like to withdraw, deposit, or exit? (W/D/E): ").strip().lower()

        if not check_withdrawal():
            return

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
            return

        else:
            print("Invalid option. Please enter W, D, or E.")


def drug_menu():
    if not check_withdrawal():
        return

    if not inventory:
        print("Your inventory is empty.")
        return

    print("=== Your Drugs ===")
    for idx, item in enumerate(inventory, start=1):
        drug_name = item["name"] if isinstance(item, dict) else item
        print(f"  {idx}) {drug_name}")

    while is_alive:
        if not check_withdrawal():
            return

        choice = input("Enter a drug name to use (or 'back' to return): ").strip()
        if choice.lower() in ("back", "cancel", ""):
            return

        if not check_withdrawal():
            return

        for idx, item in enumerate(inventory):
            drug_name = item["name"] if isinstance(item, dict) else item
            if choice.lower() == drug_name.lower():
                inventory.pop(idx)
                print(f"You used {drug_name}!")
                for drug in drugs:
                    if drug["name"] == drug_name:
                        start_or_reset_withdrawal(drug["withdraw_time"])
                return

        print("You don't have that drug in your inventory. Try again.")


def info():
    if not check_withdrawal():
        return

    if withdrawal_time is None:
        timer_text = "no active timer yet (game timer starts after your first drug)"
    else:
        remaining = max(0, int(withdrawal_time - time.monotonic()))
        timer_text = f"{remaining}s left before you die"

    print(
        f"You currently have {timer_text}\n"
        f"{format_money(money_in_bank)} in the bank\n"
        f"{format_money(money)} in your wallet\n"
        f"If you don't know how to play all you gotta do is take money from your bank into your wallet\n"
        f"Either Buy Drugs or Steal them from your dealer(if you fail the dealer kills you)\n"
        f"after you use your first drug the withdraw timer starts and you need to keep using drugs before it end and if it ends you die.\n"
        f"thats all you need to know and you can look around the menu\n"
        f"game does not start until first drug is used."
    )
    time.sleep(2)


def buy_drug():
    global money

    if not check_withdrawal():
        return

    list_drugs(drugs)
    while is_alive:
        if not check_withdrawal():
            return

        option = input("Please enter Drug Name (or 'cancel' to go back): ").strip()
        if option.lower() in ("cancel", "back", ""):
            print("Cancelled.")
            return

        if not check_withdrawal():
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
                        else:
                            print("YOU DO NOT HAVE THE FUNDS U BROKE PERSON")
                        return
                    elif confirm in ("no", "n"):
                        print("OK")
                        return
                    else:
                        print("Invalid Option. Please enter Y or N.")

        print("Drug not found. Try again.")


def format_money(amount):
    return f"${amount}"


def list_drugs(drug_list):
    print("=== For Sale ===")
    for drug in drug_list:
        print(f"=== {drug['name']}, Price: {format_money(drug['cost'])} ===")


def steal_from_dealer(inventory, dealers_inventory, success_chance=1):
    global dealers_name, is_alive

    if not check_withdrawal():
        return False

    if not dealers_inventory:
        print("they got nothing u stole all of it")
        return False

    if random.random() < success_chance:
        item = dealers_inventory.pop(0)
        inventory.append(item)
        print(f"You got {inventory[-1]}")
        return True
    else:
        print("The Dealer caught you pickpocketing and killed you.")
        is_alive = False
        return False


def main():
    random_dealer_inventory(dealers_inventory, drugs)
    print(
        f"Welcome to drug simulator!\n"
        f"You start off with {format_money(money_in_bank)} but its in your bank so you need to withdraw it\n"
        f"and need to be on a drugs before the last one weres off and you go into withdraw.\n"
        f"you are also {name} and {age} years old\n"
        f"the game starts in 3 seconds\n3"
    )
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    menu()


def menu():
    while is_alive:
        if not check_withdrawal():
            break

        print("""===============================
=== PLEASE SELECT AN OPTION ===
===============================
  1) DEALER
  2) BANK
  3) DRUGS
  4) INFO
===============================""")
        option = input("> ").strip()

        if not check_withdrawal():
            break

        if option == "1":
            dealer()
        elif option == "2":
            bank()
        elif option == "3":
            drug_menu()
        elif option == "4":
            info()
        else:
            print("INVALID OPTION")


main()