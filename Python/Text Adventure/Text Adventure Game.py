
#### ONLY THE WARRIOR CLASS IS IMPLEMENTED FOR NOW THE OTHER CLASSES SKILLS ARE NOT IMPLEMENTED YET


import random

# Ensure player structure is properly defined
if "player" not in globals():
    player = {
        "name": "Adventurer",
        "class": "a",  # Default class, can be changed during character creation
        "health": 20,
        "max_health": 20,
        "damage": 5,
        "defense": 0,
        "dexterity": 12,  # Default dexterity for initiative rolls
        "skills": [],  # Skills will be populated based on class
        "player_gold": 50,
        "score": 50,  # Ensure score is initialized to the same value as player_gold
        "keys": 0  # Track the number of keys the player has
    }

# Update player_gold and score to always reference the same value
def update_gold_and_score(amount):
    player["player_gold"] += amount
    player["score"] = player["player_gold"]

def rest(current_health, base_health):
    if current_health < base_health:
        heal_amount = random.randint(5, 15)
        current_health = min(current_health + heal_amount, base_health)
        print(f"You rest and recover {heal_amount} health. Current health: {current_health}.")
    else:
        print("You are already at full health!")
    return current_health

if "base_health" not in globals():
    base_health = player["max_health"]

def player_gold():
    pass

# Ensure skill_uses is initialized
if "skill_uses" not in globals():
    skill_uses = {
        "Power Strike": 3,
        "Shield Block": 3,
        "Quick Stab": 3,
        "Fireball": 2,
        "Arcane Shield": 3,
        "Backstab": 3,
        "Evasion": 3,
        "Heal": 3,
        "Divine Smite": 3,
        "Inspire": 3,
        "Song of Rest": 3
    }

# Ensure shop_items is initialized
if "shop_items" not in globals():
    shop_items = {
        "healing potion": {"price": 50, "description": "Restores 10 HP."},
        "armor": {"price": 100, "description": "Increases defense by 2."},
        "weapon": {"price": 150, "description": "Upgrades your weapon to deal +2 damage."}
    }

# Ensure damage_types is defined
if "damage_types" not in globals():
    damage_types = {
        "Bludgeoning": ["Hammer", "Mace"],
        "Piercing": ["Dagger", "Spear", "Arrow"],
        "Slashing": ["Sword", "Axe"],
        "Elemental": ["Fireball", "Lightning Bolt"],
        "Magical": ["Necrotic Touch", "Psychic Blast"]
    }

# Ensure roll_initiative function is defined
if "roll_initiative" not in globals():
    def roll_initiative(entity):
        return random.randint(1, 20) + calculate_modifier(entity["dexterity"])

# Ensure calculate_modifier function is defined
if "calculate_modifier" not in globals():
    def calculate_modifier(score):
        return (score - 10) // 2

# Ensure calculate_base_damage function is defined
if "calculate_base_damage" not in globals():
    def calculate_base_damage(weapon, stats):
        weapon_damage = {
            "Sword": 6,
            "Staff": 4,
            "Dagger": 5,
            "Mace": 5,
            "Lute": 3,
            "Hammer": 7,
            "Spear": 6,
            "Axe": 6
        }
        weapon_stat_map = {
            "Sword": "Strength",
            "Staff": "Intelligence",
            "Dagger": "Dexterity",
            "Mace": "Wisdom",
            "Lute": "Charisma",
            "Hammer": "Strength",
            "Spear": "Dexterity",
            "Axe": "Strength"
        }
        stat = weapon_stat_map.get(weapon, "Strength")
        return weapon_damage.get(weapon, 0) + calculate_modifier(stats.get(stat, 0))

def calculate_damage(attacker, attack_type, critical=False):
    """
    Calculates the damage dealt by an attacker based on their stats, attack type, and critical hit status.
    """
    base_damage = attacker["damage"]
    if critical:
        base_damage *= 2  
    return base_damage

# Ensure damage types are defined before they are used
damage_types = {
    "Bludgeoning": ["Mace", "Hammer", "Shield Bash"],
    "Piercing": ["Dagger", "Spear", "Arrow"],
    "Slashing": ["Sword", "Axe", "Whip"],
    "Elemental": ["Fireball", "Lightning Bolt", "Acid Splash"],
    "Magical": ["Necrotic Touch", "Psychic Blast", "Radiant Smite"]
}

# Class bonuses
class_bonuses = {
    "a": {"Strength": 2, "Weapon": "Sword", "Base Damage": 6, "Base Health": 12},
    "b": {"Intelligence": 2, "Weapon": "Staff", "Base Damage": 4, "Base Health": 8},
    "c": {"Dexterity": 2, "Weapon": "Dagger", "Base Damage": 5, "Base Health": 10},
    "d": {"Wisdom": 2, "Weapon": "Mace", "Base Damage": 5, "Base Health": 10},
    "e": {"Charisma": 2, "Weapon": "Lute", "Base Damage": 3, "Base Health": 8},
}

# Class skills
class_skills = {
    "a": ["Power Strike", "Shield Block"],
    "b": ["Fireball", "Arcane Shield"],
    "c": ["Backstab", "Evasion"],
    "d": ["Heal", "Divine Smite"],
    "e": ["Inspire", "Song of Rest"]
}

#### WARRIORS
def Power_Strike(attacker, defender):
    """
    Executes a Power Strike attack, dealing extra damage.
    """
    damage = calculate_damage(attacker, "melee", critical=False) + 3  # Extra damage for Power Strike
    defender["health"] -= damage
    print(f"{attacker['name']} uses Power Strike! Deals {damage} damage to {defender['name']}.")
    return damage

# Define a function for Shield Block, which reduces damage taken while still allowing a counterattack
def Shield_Block(attacker, defender):
    """
    Executes a Shield Block, reducing damage taken from the next attack.
    """
    print(f"{attacker['name']} braces with their shield!")
    defender["damage"] = max(0, defender["damage"] - 2)  # Reduce damage by 2 for the next attack
    return defender["damage"]

#### MAGES
# Define a function for Fireball, which deals area damage to multiple enemies
def Fireball(attacker, enemies):
    """
    Executes a Fireball attack, dealing area damage to multiple enemies.
    """
    damage = calculate_damage(attacker, "elemental", critical=False) + 5  # Extra damage for Fireball
    for enemy in enemies:
        enemy["health"] -= damage
        print(f"{attacker['name']} casts Fireball! Deals {damage} damage to {enemy['name']}.")
    return damage

# Define a function for Arcane Shield, which provides temporary damage resistance for the next two turns.
def Arcane_Shield(attacker):
    """
    Executes an Arcane Shield, providing temporary damage resistance.
    """
    print(f"{attacker['name']} casts Arcane Shield!")
    attacker["damage"] = max(0, attacker["damage"] - 2)  # Reduce damage by 2 for the next two turns
    return attacker["damage"]

#### ROGUES
# Define a function for Backstab, which deals extra damage if the target is surprised
def Backstab(attacker, defender):
    """
    Executes a Backstab attack, guarenteeing a hit and dealing extra damage.
    """
    damage = calculate_damage(attacker, "melee", critical=False) + 5  # Extra damage for Backstab
    defender["health"] -= damage
    print(f"{attacker['name']} performs a Backstab! Deals {damage} damage to {defender['name']}.")
    return damage

# Define a function for Evasion, which allows the rogue to dodge an attack and counterattack
def Evasion(attacker, defender):
    """
    Executes an Evasion, allowing the rogue to dodge an attack and counterattack.
    """
    print(f"{attacker['name']} evades the attack!")
    damage = calculate_damage(attacker, "melee", critical=False)  # Normal damage for counterattack
    defender["health"] -= damage
    print(f"{attacker['name']} counterattacks! Deals {damage} damage to {defender['name']}.")
    return damage

def make_attack_roll(attacker, defender, attack_type):
    """
    Simulates an attack roll to determine if the attack hits, critically hits, or misses.
    """
    attack_roll = random.randint(1, 20) + calculate_modifier(attacker["dexterity"])
    if attack_roll == 20:  # Natural 20 is a critical hit
        return "critical"
    elif attack_roll >= defender["armor_class"]:  # Attack roll meets or exceeds armor class
        return "hit"
    else:  # Attack roll is less than armor class
        return "miss"

# Define a function to roll stats (4d6, drop the lowest)
def roll_stat():
    rolls = [random.randint(1, 6) for _ in range(4)]
    rolls.remove(min(rolls))  # Drop the lowest die
    return sum(rolls)

# Define a function to calculate health
def calculate_health(base_health, constitution):
    modifier = calculate_modifier(constitution)
    return base_health + (modifier * 2)  # Constitution modifier directly impacts health

# Define a function to get damage type
def get_damage_type(weapon_or_skill):
    for damage_type, items in damage_types.items():
        if weapon_or_skill in items:
            return damage_type
    return "Unknown"

# Define a function to display the shop and handle purchases
def visit_shop(player_gold):
    print("Welcome to the shop! Here are the items available for purchase:")
    for item, details in shop_items.items():
        print(f"- {item.title()} (Price: {details['price']} gold): {details['description']}")
    print(f"You have {player['player_gold']} gold.")
    
    while True:
        print("What would you like to buy? (type 'leave' to exit the shop)")
        item_choice = input().lower()
        if item_choice == "leave":
            print("You leave the shop.")
            break
        elif item_choice in shop_items:
            item_price = shop_items[item_choice]["price"]
            if player_gold >= item_price:
                update_gold_and_score(-item_price)
                print(f"You bought a {item_choice} for {item_price} gold. You now have {player['player_gold']} gold.")
                # Add item effects here if needed
                if item_choice == "healing potion":
                    print("You store the healing potion in your inventory.")
                elif item_choice == "armor":
                    print("Your defense has increased!")
                elif item_choice == "weapon":
                    print("Your weapon has been upgraded!")
            else:
                print("You don't have enough gold to buy that item.")
        else:
            print("Invalid choice. Please select an item from the shop.")
        print(f"Current gold: {player['player_gold']}")  # Display player's gold after each action
    return player_gold

# Function to explore a dungeon room
def explore_room():
    print("\nYou enter a dark room in the dungeon.")
    room_events = [
        "You find a treasure chest!",
        "You encounter a locked door.",
        "A goblin ambushes you!",
        "You find a healing fountain.",
        "The room is empty, but eerie noises surround you."
    ]
    event = random.choice(room_events)
    print(event)

    if event == "You find a treasure chest!":
        gold_found = random.randint(10, 50)
        update_gold_and_score(gold_found)
        print(f"You open the chest and find {gold_found} gold! You have {player['player_gold']} gold now.")
    elif event == "You encounter a locked door.":
        if player["keys"] > 0:
            print("You use a key to unlock the door and proceed.")
            player["keys"] -= 1
        else:
            print("The door is locked. You need a key to open it.")
    elif event == "A goblin ambushes you!":
        tutorial_goblin_fight(player, skill_uses)
        print("After defeating the goblin, you find a key!")
        player["keys"] += 1
    elif event == "You find a healing fountain.":
        heal_amount = random.randint(5, 15)
        player["health"] = min(player["health"] + heal_amount, player["max_health"])
        print(f"You drink from the fountain and heal {heal_amount} health. Your health is now {player['health']}.")
    elif event == "The room is empty, but eerie noises surround you.":
        print("You feel uneasy but nothing happens.")

def tutorial_goblin_fight(player, skill_uses):
    print("\nAs you explore, you hear a scream nearby!")
    print("You rush to the scene and see a villager being attacked by a goblin!")
    print("This is a tutorial fight to teach you how combat works.")

    goblin = {
        "name": "Goblin",
        "health": 15,
        "damage": 3,
        "armor_class": 6,
        "dexterity": 12,
        "attacks": [
            {"damage": 3, "type": "Slashing", "description": "The goblin slashes at you with its claws!"},
            {"damage": 4, "type": "Piercing", "description": "The goblin stabs at you with a rusty dagger!"},
            {"damage": 2, "type": "Bludgeoning", "description": "The goblin bashes you with a club!"}
        ]
    }

    # Roll initiative
    player_initiative = roll_initiative(player)
    goblin_initiative = roll_initiative(goblin)
    print(f"\nInitiative rolls: You rolled {player_initiative}, the goblin rolled {goblin_initiative}.")

    # Determine turn order
    turn_order = ["player", "goblin"] if player_initiative >= goblin_initiative else ["goblin", "player"]

    # Combat loop
    round_number = 1
    while player["health"] > 0 and goblin["health"] > 0:
        print(f"\n--- Round {round_number} ---")
        for turn in turn_order:
            if turn == "player":
                print(f"\nYour turn! Your health: {player['health']}, Goblin's health: {goblin['health']}")
                print("Choose your action:")
                print("1. Basic Attack")
                print("2. Defend")
                print("3. Use Skill")
                print("4. Run")
                action = input("Enter the number of your action: ")

                if action == "1":  # Attack
                    print("Choose your attack type:")
                    print("1. Slash (Slashing damage)")
                    print("2. Stab (Piercing damage)")
                    print("3. Bash (Bludgeoning damage)")
                    attack_choice = input("Enter the number of your attack: ")

                    attack_type = "melee"  # Default to melee attacks
                    attack_result = make_attack_roll(player, goblin, attack_type)

                    if attack_result == "hit":
                        critical = False
                        damage = calculate_damage(player, attack_type, critical)
                        goblin["health"] -= damage
                        print(f"You deal {damage} damage to the goblin!")
                    elif attack_result == "critical":
                        damage = calculate_damage(player, attack_type, critical=True)
                        goblin["health"] -= damage
                        print(f"You deal {damage} critical damage to the goblin!")
                    elif attack_result == "miss":
                        print("Your attack misses!")

                elif action == "2":  # Defend
                    print("You brace yourself for the goblin's attack, reducing incoming damage!")

                elif action == "3":  # Use Skill
                    print("Choose a skill to use:")
                    # Filter skills based on the player's class and remaining uses
                    available_skills = [skill for skill in class_skills[player["class"]] if skill_uses[skill] > 0]
                    if not available_skills:
                        print("You have no skills available to use!")
                        continue
                    # Display available skills
                    for skill in available_skills:
                        print(f"{skill} (Uses left: {skill_uses[skill]})")
                    skill_choice = input("Enter the name of the skill: ").strip()
                    if skill_choice in available_skills:
                        skill_uses[skill_choice] -= 1
                        # Execute the selected skill
                        if skill_choice == "Power Strike":
                            Power_Strike(player, goblin)
                        elif skill_choice == "Shield Block":
                            Shield_Block(player, goblin)
                        elif skill_choice == "Fireball":
                            Fireball(player, [goblin])
                        elif skill_choice == "Arcane Shield":
                            Arcane_Shield(player)
                        elif skill_choice == "Backstab":
                            Backstab(player, goblin)
                        elif skill_choice == "Evasion":
                            Evasion(player, goblin)
                        elif skill_choice == "Heal":
                            heal_amount = random.randint(5, 15)
                            player["health"] = min(player["health"] + heal_amount, player["max_health"])
                            print(f"You heal {heal_amount} health. Your health is now {player['health']}.")
                        elif skill_choice == "Divine Smite":
                            damage = calculate_damage(player, "magical", critical=False) + 5
                            goblin["health"] -= damage
                            print(f"You deal {damage} radiant damage to the goblin!")
                        elif skill_choice == "Inspire":
                            print("You inspire your allies!")
                        elif skill_choice == "Song of Rest":
                            print("You play a soothing melody, restoring some health.")
                    else:
                        print("Invalid skill choice. Please choose a valid skill.")

                elif action == "4":  # Run
                    print("You attempt to flee!")
                    if random.randint(1, 20) > 5:
                        print("You successfully escape!")
                        return
                    else:
                        print("The goblin blocks your escape!")
                else:
                    print("Invalid action. Please choose again.")
                    continue

                if goblin["health"] <= 0:
                    print("You defeated the goblin and saved the villager!")
                    update_gold_and_score(10)  # Add score for defeating the goblin
                    return

            elif turn == "goblin":
                print(f"\nThe goblin's turn!")
                goblin_attack = random.choice(goblin["attacks"])
                print(goblin_attack["description"])
                damage = max(0, goblin_attack["damage"] - player.get("defense", 0))
                player["health"] -= damage
                print(f"The goblin deals {damage} {goblin_attack['type']} damage to you!")
                if player["health"] <= 0:
                    print("You were defeated by the goblin. Game over.")
                    exit()

        round_number += 1

# Game starts here
print("Welcome to the Dungeon Explorer!")
print("In this game, you will create a character, explore a dangerous dungeon, and face various challenges.")
print("Your goal is to survive, gather treasure, and defeat the fearsome dragon Hugh Jackman!")
print("\nBefore we begin, here's an explanation of the stats you'll be working with:")
print("""
- Strength: Determines your physical power and affects melee weapon damage.
- Dexterity: Represents agility and reflexes, affecting ranged attacks and dodging.
- Constitution: Measures endurance and affects your total health.
- Intelligence: Represents knowledge and reasoning, useful for magic and problem-solving.
- Wisdom: Reflects perception and insight, aiding in spotting traps or hidden details.
- Charisma: Represents charm and influence, useful for persuasion and social interactions.
""")
print("You will roll for these stats and assign them to your character. Choose wisely!")
print("\nDo you want to play the game? (yes/no)")
play_game = input().lower()
if play_game != "yes":
    print("Goodbye!")
    exit()

# Step 1: Roll and assign stats
print("Rolling stats...")
rolled_stats = [roll_stat() for _ in range(6)]
print(f"Your rolled stats: {rolled_stats}")
stats = {"Strength": 0, "Dexterity": 0, "Constitution": 0, "Intelligence": 0, "Wisdom": 0, "Charisma": 0}

print("Assign your rolled stats to the following abilities:")
for stat in stats.keys():
    while True:
        try:
            print(f"Available stats: {rolled_stats}")
            assigned_stat = int(input(f"Assign a value to {stat}: "))
            if assigned_stat in rolled_stats:
                stats[stat] = assigned_stat
                rolled_stats.remove(assigned_stat)
                break
            else:
                print("Invalid choice. Please choose from the available stats.")
        except ValueError:
            print("Please enter a valid number.")

print(f"Your final stats: {stats}")

# Step 2: Choose character class
print("Choose your character class. Press 1 to see the classes and their descriptions.")
choice = input().lower()

if choice == "1":
    print("""
    a) The Warrior - gets a sword and +2 strength. Skills: Power Strike, Shield Block.
    b) The Mage - gets a staff and +2 intelligence. Skills: Fireball, Arcane Shield.
    c) The Rogue - gets a dagger and +2 dexterity. Skills: Backstab, Evasion.
    d) The Cleric - gets a mace and +2 wisdom. Skills: Heal, Divine Smite.
    e) The Bard - gets a lute and +2 charisma. Skills: Inspire, Song of Rest.
    """)
    print("Now choose your class:")
    choice = input().lower()

if choice in class_bonuses:
    selected_class = class_bonuses[choice]
    for key, value in selected_class.items():
        if key in stats:
            stats[key] += value
    weapon = selected_class["Weapon"]
    base_damage = selected_class["Base Damage"]
    base_health = selected_class["Base Health"]
    print(f"You chose {weapon} class! Your stats have been updated: {stats}")

    damage = calculate_base_damage(weapon, stats)  # Use the primary stat for the weapon
    damage_type = get_damage_type(weapon) 
    health = calculate_health(base_health, stats["Constitution"])  # Base health scales with Constitution

    print(f"Your weapon is a {weapon}. It deals {damage} {damage_type} damage.")
    print(f"Your total health is {health}.")
else:
    print("Invalid choice. Please restart the game.")
    exit()

# Step 3: Assign character name
character_name = input("Enter your character's name: ")
print(f"Welcome, {character_name} the {weapon} wielder!")

if choice in class_skills:
    skills = class_skills[choice]
    print(f"As a {weapon} wielder, you have the following skills: {', '.join(skills)}")
else:
    print("No skills assigned.")

# Step 4: Tavern and world-building
print("You find yourself in a dimly lit tavern. The smell of ale and roasted meat fills the air.")
print("The tavern is abuzz with adventurers sharing tales of their exploits.")
print("You overhear a group talking about the dragon Hugh Jackman, a fearsome beast known for his hoard of treasure.")
print("Hugh Jackman is said to dwell deep within a dungeon filled with traps and monsters.")
print("The dungeon is rumored to contain hazards dealing various types of damage:")

# Step 5: Player options
while True:
    print("\nWhat would you like to do next? (explore/shop/gather/rest/quit)")
    choice = input().lower()

    if choice == "explore":
        explore_room()
    elif choice == "shop":
        player_gold = visit_shop(player_gold)
    elif choice == "gather":
        print("You gather information from the adventurers in the tavern.")
        print("They warn you about traps and monsters in the dungeon.")
        print("""
            - Bludgeoning: Falling rocks and crushing walls.
            - Piercing: Spiked traps and arrow volleys.
            - Slashing: Whirling blades and monster claws.
            - Elemental: Acid pools, fire traps, and lightning strikes.
            - Magical: Necrotic curses, psychic attacks, and radiant blasts.""")
    elif choice == "rest":
        health = rest(player["health"], base_health)
        player["health"] = health
    elif choice == "quit":
        print(f"Thank you for playing! Your final score is {player['score']}.")
        break
    else:
        print("Invalid choice. Please choose again.")