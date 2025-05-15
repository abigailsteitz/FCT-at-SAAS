import random

# Ensure player structure is properly defined
if "player" not in globals():
    player = {
        "name": "Adventurer",
        "class": "a",  # Default class, can be changed during character creation
        "health": 0,  # Health will be calculated based on Constitution
        "max_health": 0,  # Max health will also be calculated
        "damage": 5,
        "defense": 0,
        "dexterity": 12,  # Default dexterity for initiative rolls
        "skills": [],  # Skills will be populated based on class
        "player_gold": 50,
        "score": 50,  # Ensure score is initialized to the same value as player_gold
        "keys": 0,  # Track the number of keys the player has
        "xp": 0,
        "level": 1
    }

# Update player_gold and score to always reference the same value
def update_gold_and_score(amount):
    player["player_gold"] += amount
    player["score"] = player["player_gold"]

# Function to calculate health based on Constitution
def calculate_health(base_health, constitution):
    modifier = calculate_modifier(constitution)
    return base_health + (modifier * 2)  # Constitution modifier directly impacts health

# Initialize health after stats and class selection
def initialize_health():
    player["max_health"] = calculate_health(base_health, stats["Constitution"])
    player["health"] = player["max_health"]

# Rest function to recover health
def rest(current_health, max_health):
    if current_health < max_health:
        heal_amount = random.randint(5, 15)
        current_health = min(current_health + heal_amount, max_health)
        print(f"You rest and recover {heal_amount} health. Current health: {current_health}.")
    else:
        print("You are already at full health!")
    return current_health

if "base_health" not in globals():
    base_health = player["max_health"]

def player_gold():
    pass


# Ensure shop_items is initialized
if "shop_items" not in globals():
    shop_items = {
        "healing potion": {"price": 50, "description": "Restores 10 HP."},
        "armor": {"price": 100, "description": "Increases defense by 2."},
        "weapon": {"price": 150, "description": "Upgrades your weapon to deal +2 damage."},
        "key": {"price": 75, "description": "Unlocks locked doors in the dungeon."}
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

# Add all class skills
def Divine_Smite(attacker, defender):
    """
    Executes Divine Smite, dealing radiant damage.
    """
    damage = calculate_damage(attacker, "magical", critical=False) + 5
    defender["health"] -= damage
    print(f"{attacker['name']} uses Divine Smite! Deals {damage} radiant damage to {defender['name']}.")
    return damage

def Inspire(attacker):
    """
    Executes Inspire, boosting the player's stats temporarily.
    """
    print(f"{attacker['name']} inspires their allies! Your stats temporarily increase.")
    attacker["damage"] += 2
    attacker["defense"] += 1
    return True

def Song_of_Rest(attacker):
    """
    Executes Song of Rest, healing the player.
    """
    heal_amount = random.randint(10, 20)
    attacker["health"] = min(attacker["health"] + heal_amount, attacker["max_health"])
    print(f"{attacker['name']} sings a Song of Rest, healing {heal_amount} health. Current health: {attacker['health']}.")
    return heal_amount

def Holy_Light(attacker, allies):
    """
    Heals all allies in the party.
    """
    heal_amount = random.randint(8, 15)
    for ally in allies:
        ally["health"] = min(ally["health"] + heal_amount, ally["max_health"])
        print(f"{attacker['name']} uses Holy Light, healing {heal_amount} health for {ally['name']}.")
    return heal_amount

def Poison_Blade(attacker, defender):
    """
    Applies poison damage over time to the defender.
    """
    poison_damage = random.randint(3, 6)
    defender["health"] -= poison_damage
    print(f"{attacker['name']} uses Poison Blade! Deals {poison_damage} poison damage to {defender['name']}.")
    return poison_damage

def Shadow_Step(attacker, defender):
    """
    Allows the attacker to evade and counterattack.
    """
    print(f"{attacker['name']} uses Shadow Step to evade and counterattack!")
    damage = calculate_damage(attacker, "melee", critical=False) + 4
    defender["health"] -= damage
    print(f"{attacker['name']} counterattacks, dealing {damage} damage to {defender['name']}.")
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

#### EXPANDED GAME WITH LEVELING, CHARISMA INTERACTIONS, AND OPEN-ENDED EVENTS

import random

# Add experience and leveling system
if "player_xp" not in globals():
    player["xp"] = 0
    player["level"] = 1

def level_up():
    player["level"] += 1
    print(f"\nCongratulations! You leveled up to Level {player['level']}!")
    print("Choose a stat to improve:")
    print("1. Strength")
    print("2. Dexterity")
    print("3. Constitution")
    print("4. Intelligence")
    print("5. Wisdom")
    print("6. Charisma")
    while True:
        choice = input("Enter the number of the stat to improve: ")
        if choice in ["1", "2", "3", "4", "5", "6"]:
            stat_map = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]
            selected_stat = stat_map[int(choice) - 1]
            stats[selected_stat] += 1
            print(f"{selected_stat} increased to {stats[selected_stat]}!")
            break
        else:
            print("Invalid choice. Please select a valid stat.")

    # Unlock new skills based on class
    new_skills = {
        "a": ["Whirlwind Strike", "Shield Bash"],
        "b": ["Meteor Shower", "Mana Shield"],
        "c": ["Shadow Step", "Poison Blade"],
        "d": ["Holy Light", "Guardian Angel"],
        "e": ["Battle Hymn", "Encore"]
    }
    if player["class"] in new_skills:
        unlocked_skill = random.choice(new_skills[player["class"]])
        player["skills"].append(unlocked_skill)
        skill_uses[unlocked_skill] = 3
        print(f"You unlocked a new skill: {unlocked_skill}!")

# Update combat to include XP rewards and key mechanics
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
                    available_skills = [skill for skill in class_skills[player["class"]] if skill_uses[skill] > 0]
                    if not available_skills:
                        print("You have no skills available to use!")
                        continue
                    for skill in available_skills:
                        print(f"{skill} (Uses left: {skill_uses[skill]})")
                    skill_choice = input("Enter the name of the skill: ").strip()
                    if skill_choice in available_skills:
                        skill_uses[skill_choice] -= 1
                        if skill_choice == "Power Strike":
                            Power_Strike(player, goblin)
                        elif skill_choice == "Shield Block":
                            Shield_Block(player, goblin)
                        # Add logic for new skills here
                    else:
                        print("Invalid skill choice. Please choose a valid skill.")

                elif action == "4":  # Run
                    print("You attempt to flee!")
                    if random.randint(1, 20) > 10:
                        print("You successfully escape!")
                        return
                    else:
                        print("The goblin blocks your escape!")
                else:
                    print("Invalid action. Please choose again.")
                    continue

                if goblin["health"] <= 0:
                    print("You defeated the goblin and saved the villager!")
                    player["xp"] += 10  # Add XP for defeating the goblin
                    print(f"You gained 10 XP! Total XP: {player['xp']}")
                    if player["xp"] >= player["level"] * 10:
                        level_up()
                    player["keys"] += 1  # Add key for defeating the goblin
                    print("You found a key!")
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

# Add charisma-based interactions in town
def visit_town():
    print("\nYou arrive at a bustling town filled with merchants, adventurers, and townsfolk.")
    if stats["Charisma"] >= 15:
        print("Your high Charisma attracts attention. People are eager to help you!")
        print("You gain a free healing potion from a kind merchant.")
        player["inventory"].append("healing potion")
    else:
        print("The townsfolk seem indifferent to you. You browse the shops quietly.")

# Add deeper dungeon events
def explore_deeper_dungeon():
    print("\nYou venture deeper into the dungeon. The air grows hotter, and the walls seem to pulse with energy.")
    deeper_events = [
        "You encounter a lava pit. A fire elemental emerges!",
        "You find a mysterious altar. Do you pray or leave it alone?",
        "You hear whispers of 'boiling the ocean'... What could it mean?",
        "A treasure chest lies in the corner, but it is guarded by a dragonling."
    ]
    event = random.choice(deeper_events)
    print(event)
    # Add logic for each event here

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

# Ensure skill_uses is initialized based on the selected class
def initialize_skills(player_class):
    """
    Initializes the player's skills based on their selected class.
    """
    global skill_uses
    class_skills = {
        "a": ["Power Strike", "Shield Block"],
        "b": ["Fireball", "Arcane Shield"],
        "c": ["Backstab", "Evasion"],
        "d": ["Heal", "Divine Smite"],
        "e": ["Inspire", "Song of Rest"]
    }
    skill_uses = {skill: 3 for skill in class_skills[player_class]}  # Default 3 uses per skill
    player["skills"] = class_skills[player_class]
    print(f"Skills unlocked for your class: {', '.join(player['skills'])}")

# Updated class selection to initialize skills based on the selected class
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
    base_health = selected_class["Base Health"]
    initialize_health()  # Calculate health based on Constitution
    initialize_skills(choice)  # Initialize skills based on the selected class
    print(f"You chose the {choice.upper()} class! Your stats have been updated: {stats}")
    print(f"Your health is now {player['health']} / {player['max_health']}.")
elif choice == "quit":
    print(f"Thank you for playing! Your final score is {player['score']}.")
    exit()  # Exit the game loop
else:
    print("Invalid choice. Please restart the game.")
    exit()

# Add reusable function for combat
def combat(player, enemy):
    """
    Handles combat between the player and an enemy.
    """
    print(f"\nA wild {enemy['name']} appears!")
    round_number = 1
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n--- Round {round_number} ---")
        print(f"Your health: {player['health']} / {player['max_health']}, {enemy['name']}'s health: {enemy['health']}")
        print("Choose your action:")
        print("1. Basic Attack")
        print("2. Defend")
        print("3. Use Skill")
        print("4. Run")
        action = input("Enter the number of your action: ")

        if action == "1":  # Basic Attack
            attack_result = make_attack_roll(player, enemy, "melee")
            if attack_result == "hit":
                damage = calculate_damage(player, "melee")
                enemy["health"] -= damage
                print(f"You deal {damage} damage to the {enemy['name']}!")
            elif attack_result == "critical":
                damage = calculate_damage(player, "melee", critical=True)
                enemy["health"] -= damage
                print(f"You deal {damage} critical damage to the {enemy['name']}!")
            else:
                print("Your attack misses!")

        elif action == "2":  # Defend
            print("You brace yourself, reducing incoming damage!")

        elif action == "3":  # Use Skill
            print("Choose a skill to use:")
            available_skills = [skill for skill in player["skills"] if skill_uses[skill] > 0]
            if not available_skills:
                print("You have no skills available to use!")
                continue
            for skill in available_skills:
                print(f"{skill} (Uses left: {skill_uses[skill]})")
            skill_choice = input("Enter the name of the skill: ").strip()
            if skill_choice in available_skills:
                skill_uses[skill_choice] -= 1
                if skill_choice == "Power Strike":
                    Power_Strike(player, enemy)
                elif skill_choice == "Shield Block":
                    Shield_Block(player, enemy)
                elif skill_choice == "Fireball":
                    Fireball(player, [enemy])
                elif skill_choice == "Arcane Shield":
                    Arcane_Shield(player)
                elif skill_choice == "Backstab":
                    Backstab(player, enemy)
                elif skill_choice == "Evasion":
                    Evasion(player, enemy)
                elif skill_choice == "Heal":
                    Song_of_Rest(player)
                elif skill_choice == "Divine Smite":
                    Divine_Smite(player, enemy)
                elif skill_choice == "Inspire":
                    Inspire(player)
                elif skill_choice == "Song of Rest":
                    Song_of_Rest(player)
            else:
                print("Invalid skill choice. Please choose a valid skill.")

        elif action == "4":  # Run
            print("You attempt to flee!")
            if random.randint(1, 20) > 10:
                print("You successfully escape!")
                return False
            else:
                print("The enemy blocks your escape!")

        else:
            print("Invalid action. Please choose again.")
            continue

        # Enemy's turn
        if enemy["health"] > 0:
            print(f"\nThe {enemy['name']}'s turn!")
            enemy_attack = random.choice(enemy.get("attacks", [{"damage": enemy["damage"], "description": "The enemy attacks!"}]))
            print(enemy_attack["description"])
            damage = max(0, enemy_attack["damage"] - player.get("defense", 0))
            player["health"] -= damage
            print(f"The {enemy['name']} deals {damage} damage to you!")

        if player["health"] <= 0:
            print("You were defeated. Game over.")
            exit()

        round_number += 1

    if enemy["health"] <= 0:
        print(f"You defeated the {enemy['name']}!")
        player["xp"] += enemy.get("xp_reward", 10)
        print(f"You gained {enemy.get('xp_reward', 10)} XP! Total XP: {player['xp']}")
        if player["xp"] >= player["level"] * 10:
            level_up()
        return True

# Add dungeon events
def dungeon_event():
    """
    Handles random events in the dungeon with reduced repetition.
    """
    events = [
        "You find a treasure chest!",
        "You encounter a locked door.",
        "A goblin ambushes you!",
        "You find a healing fountain.",
        "You stumble into a trap!",
        "A wandering merchant offers you rare items.",
        "You hear eerie whispers in the dark.",
        "You find a strange glowing crystal.",
        "You encounter a group of skeletons guarding a treasure.",
        "You find a hidden alcove with a mysterious artifact."
    ]
    event = random.choice(events)
    events.remove(event)  # Reduce repetition by removing the event from the list
    print(f"\n{event}")

    if event == "You find a treasure chest!":
        gold_found = random.randint(10, 50)
        update_gold_and_score(gold_found)
        print(f"You open the chest and find {gold_found} gold! You now have {player['player_gold']} gold.")

    elif event == "You encounter a locked door.":
        if player["keys"] > 0:
            print("You use a key to unlock the door and proceed.")
            player["keys"] -= 1
        else:
            print("The door is locked. You need a key to open it.")

    elif event == "A goblin ambushes you!":
        goblin = {
            "name": "Goblin",
            "health": 15,
            "damage": 3,
            "armor_class": 6,
            "dexterity": 12,
            "xp_reward": 10,
            "attacks": [
                {"damage": 3, "type": "Slashing", "description": "The goblin slashes at you with its claws!"},
                {"damage": 4, "type": "Piercing", "description": "The goblin stabs at you with a rusty dagger!"},
                {"damage": 2, "type": "Bludgeoning", "description": "The goblin bashes you with a club!"}
            ]
        }
        combat(player, goblin)

    elif event == "You find a healing fountain.":
        heal_amount = random.randint(5, 15)
        player["health"] = min(player["health"] + heal_amount, player["max_health"])
        print(f"You drink from the fountain and heal {heal_amount} health. Your health is now {player['health']}.")

    elif event == "You stumble into a trap!":
        trap_damage = random.randint(5, 10)
        player["health"] -= trap_damage
        print(f"A trap is triggered! You take {trap_damage} damage. Your health is now {player['health']}.")

    elif event == "A wandering merchant offers you rare items.":
        print("The merchant offers you a rare healing potion for 30 gold.")
        if player["player_gold"] >= 30:
            choice = input("Do you want to buy it? (yes/no): ").lower()
            if choice == "yes":
                update_gold_and_score(-30)
                player["inventory"].append("healing potion")
                print("You bought the rare healing potion!")
            else:
                print("You decline the merchant's offer.")
        else:
            print("You don't have enough gold to buy the potion.")

    elif event == "You hear eerie whispers in the dark.":
        print("The whispers grow louder, but nothing happens... or does it?")

    elif event == "You find a strange glowing crystal.":
        print("The crystal emits a faint hum. You feel a surge of energy as you touch it.")
        stat_boost = random.choice(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"])
        stats[stat_boost] += 1
        print(f"Your {stat_boost} has increased by 1!")

    elif event == "You encounter a group of skeletons guarding a treasure.":
        skeletons = [
            {"name": "Skeleton", "health": 20, "damage": 4, "armor_class": 8, "dexterity": 10, "xp_reward": 15},
            {"name": "Skeleton", "health": 20, "damage": 4, "armor_class": 8, "dexterity": 10, "xp_reward": 15}
        ]
        for skeleton in skeletons:
            combat(player, skeleton)
        print("After defeating the skeletons, you find a treasure chest!")
        gold_found = random.randint(30, 70)
        update_gold_and_score(gold_found)
        print(f"You collect {gold_found} gold! You now have {player['player_gold']} gold.")

    elif event == "You find a hidden alcove with a mysterious artifact.":
        print("The artifact glows faintly. You feel its power coursing through you.")
        artifact_effect = random.choice(["health", "damage", "defense"])
        if artifact_effect == "health":
            player["max_health"] += 5
            player["health"] = player["max_health"]
            print("Your maximum health has increased by 5!")
        elif artifact_effect == "damage":
            player["damage"] += 2
            print("Your damage has increased by 2!")
        elif artifact_effect == "defense":
            player["defense"] += 2
            print("Your defense has increased by 2!")

# New combat events
def combat_event():
    """
    Handles special combat events during battles.
    """
    events = [
        "The enemy calls for reinforcements!",
        "A trap is triggered during the fight!",
        "You find an opening to deal a critical strike!",
        "The enemy drops a potion mid-fight!"
    ]
    event = random.choice(events)
    print(f"\nCombat Event: {event}")

    if event == "The enemy calls for reinforcements!":
        reinforcement = {
            "name": "Reinforcement Goblin",
            "health": 10,
            "damage": 2,
            "armor_class": 5,
            "dexterity": 10,
            "xp_reward": 5
        }
        print(f"A {reinforcement['name']} joins the fight!")
        combat(player, reinforcement)

    elif event == "A trap is triggered during the fight!":
        trap_damage = random.randint(5, 10)
        player["health"] -= trap_damage
        print(f"A hidden trap is triggered! You take {trap_damage} damage. Your health is now {player['health']}.")

    elif event == "You find an opening to deal a critical strike!":
        critical_damage = player["damage"] * 2
        print(f"You seize the opportunity and deal {critical_damage} critical damage to the enemy!")

    elif event == "The enemy drops a potion mid-fight!":
        print("The enemy drops a healing potion. You quickly pick it up and add it to your inventory.")
        player["inventory"].append("healing potion")

# Updated combat function to include combat events
def combat(player, enemy):
    """
    Handles combat between the player and an enemy with special combat events.
    """
    print(f"\nA wild {enemy['name']} appears!")
    round_number = 1
    while player["health"] > 0 and enemy["health"] > 0:
        print(f"\n--- Round {round_number} ---")
        print(f"Your health: {player['health']} / {player['max_health']}, {enemy['name']}'s health: {enemy['health']}")
        print("Choose your action:")
        print("1. Basic Attack")
        print("2. Defend")
        print("3. Use Skill")
        print("4. Use Item")
        print("5. Run")
        action = input("Enter the number of your action: ").strip()

        if action == "1":  # Basic Attack
            attack_result = make_attack_roll(player, enemy, "melee")
            if attack_result == "hit":
                damage = calculate_damage(player, "melee")
                enemy["health"] -= damage
                print(f"You deal {damage} damage to the {enemy['name']}!")
            elif attack_result == "critical":
                damage = calculate_damage(player, "melee", critical=True)
                enemy["health"] -= damage
                print(f"You deal {damage} critical damage to the {enemy['name']}!")
            else:
                print("Your attack misses!")

        elif action == "2":  # Defend
            print("You brace yourself, reducing incoming damage!")

        elif action == "3":  # Use Skill
            print("Choose a skill to use:")
            available_skills = [skill for skill in player["skills"] if skill_uses[skill] > 0]
            if not available_skills:
                print("You have no skills available to use!")
                continue
            for skill in available_skills:
                print(f"{skill} (Uses left: {skill_uses[skill]})")
            skill_choice = input("Enter the name of the skill: ").strip()
            if skill_choice in available_skills:
                skill_uses[skill_choice] -= 1
                if skill_choice == "Power Strike":
                    Power_Strike(player, enemy)
                elif skill_choice == "Shield Block":
                    Shield_Block(player, enemy)
                elif skill_choice == "Fireball":
                    Fireball(player, [enemy])
                elif skill_choice == "Arcane Shield":
                    Arcane_Shield(player)
                elif skill_choice == "Backstab":
                    Backstab(player, enemy)
                elif skill_choice == "Evasion":
                    Evasion(player, enemy)
                elif skill_choice == "Heal":
                    Song_of_Rest(player)
                elif skill_choice == "Divine Smite":
                    Divine_Smite(player, enemy)
                elif skill_choice == "Inspire":
                    Inspire(player)
                elif skill_choice == "Song of Rest":
                    Song_of_Rest(player)
            else:
                print("Invalid skill choice. Please choose a valid skill.")

        elif action == "4":  # Use Item
            use_item()

        elif action == "5":  # Run
            print("You attempt to flee!")
            if random.randint(1, 20) > 10:
                print("You successfully escape!")
                return False
            else:
                print("The enemy blocks your escape!")

        else:
            print("Invalid action. Please choose again.")
            continue

        # Trigger a random combat event
        if random.randint(1, 4) == 1:  # 25% chance of a combat event
            combat_event()

        # Enemy's turn
        if enemy["health"] > 0:
            print(f"\nThe {enemy['name']}'s turn!")
            enemy_attack = random.choice(enemy.get("attacks", [{"damage": enemy["damage"], "description": "The enemy attacks!"}]))
            print(enemy_attack["description"])
            damage = max(0, enemy_attack["damage"] - player.get("defense", 0))
            player["health"] -= damage
            print(f"The {enemy['name']} deals {damage} damage to you!")

        if player["health"] <= 0:
            print("You were defeated. Game over.")
            exit()

        round_number += 1

    if enemy["health"] <= 0:
        print(f"You defeated the {enemy['name']}!")
        player["xp"] += enemy.get("xp_reward", 10)
        print(f"You gained {enemy.get('xp_reward', 10)} XP! Total XP: {player['xp']}")
        if player["xp"] >= player["level"] * 10:
            level_up()
        return True

# Add deeper dungeon exploration
def explore_deeper_dungeon():
    """
    Handles exploration of deeper dungeon levels.
    """
    print("\nYou venture deeper into the dungeon. The air grows colder, and the walls seem to close in.")
    deeper_events = [
        "You encounter a fire elemental guarding a treasure!",
        "A shadowy figure offers you a mysterious deal.",
        "You find an ancient relic glowing with power.",
        "A dragonling blocks your path!"
    ]
    event = random.choice(deeper_events)
    print(f"\n{event}")

    if event == "You encounter a fire elemental guarding a treasure!":
        fire_elemental = {
            "name": "Fire Elemental",
            "health": 30,
            "damage": 8,
            "armor_class": 10,
            "dexterity": 8,
            "xp_reward": 20,
            "attacks": [
                {"damage": 8, "type": "Elemental", "description": "The fire elemental engulfs you in flames!"},
                {"damage": 6, "type": "Bludgeoning", "description": "The fire elemental slams into you!"}
            ]
        }
        if combat(player, fire_elemental):
            print("Behind the elemental, you find a treasure chest filled with gold!")
            gold_found = random.randint(50, 100)
            update_gold_and_score(gold_found)
            print(f"You gain {gold_found} gold! You now have {player['player_gold']} gold.")

    elif event == "A shadowy figure offers you a mysterious deal.":
        print("The figure offers to double your gold... or take it all. Do you accept?")
        choice = input("Enter 'yes' to accept or 'no' to decline: ").lower()
        if choice == "yes":
            if random.randint(1, 2) == 1:
                doubled_gold = player["player_gold"] * 2
                update_gold_and_score(doubled_gold - player["player_gold"])
                print(f"The deal succeeds! Your gold is now {player['player_gold']}.")
            else:
                update_gold_and_score(-player["player_gold"])
                print("The deal fails! You lose all your gold.")
        else:
            print("You decline the deal and move on.")

    elif event == "You find an ancient relic glowing with power.":
        print("The relic grants you a permanent stat boost!")
        stat = random.choice(["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"])
        stats[stat] += 1
        print(f"Your {stat} increases to {stats[stat]}!")

    elif event == "A dragonling blocks your path!":
        dragonling = {
            "name": "Dragonling",
            "health": 40,
            "damage": 10,
            "armor_class": 12,
            "dexterity": 10,
            "xp_reward": 30,
            "attacks": [
                {"damage": 10, "type": "Slashing", "description": "The dragonling slashes at you with its claws!"},
                {"damage": 12, "type": "Fire", "description": "The dragonling breathes fire at you!"}
            ]
        }
        combat(player, dragonling)

# Game loop
while True:
    print("\nWhat would you like to do next? (explore/shop/rest/deeper/quit)")
    choice = input().lower()

    if choice == "explore":
        dungeon_event()
    elif choice == "shop":
        visit_shop(player["player_gold"])
    elif choice == "rest":
        player["health"] = rest(player["health"], base_health)
    elif choice == "deeper":
        explore_deeper_dungeon()
    elif choice == "quit":
        print(f"Thank you for playing! Your final score is {player['score']}.")
        break
    else:
        print("Invalid choice. Please choose 'explore', 'shop', 'rest', 'deeper', or 'quit'.")

# AI system for event generation
def generate_event(depth):
    """
    Generates an event based on the dungeon depth.
    """
    if depth < 3:
        events = [
            "You find a treasure chest!",
            "A goblin ambushes you!",
            "You find a healing fountain.",
            "You stumble into a trap!"
        ]
    elif depth < 6:
        events = [
            "You encounter a locked door.",
            "A wandering merchant offers you rare items.",
            "You find an ancient relic glowing with power.",
            "A fire elemental blocks your path!"
        ]
    else:
        events = [
            "You hear the roar of the dragon in the distance.",
            "A dragonling guards the next room!",
            "You find a mysterious altar.",
            "The dragon Hugh Jackman awaits you!"
        ]
    return random.choice(events)

# Dungeon exploration system
def explore_dungeon():
    """
    Handles dungeon exploration with a linear progression toward the dragon.
    """
    depth = 1
    while True:
        print(f"\n--- Dungeon Depth: {depth} ---")
        event = generate_event(depth)
        print(event)

        if event == "You find a treasure chest!":
            gold_found = random.randint(10, 50)
            update_gold_and_score(gold_found)
            print(f"You open the chest and find {gold_found} gold! You now have {player['player_gold']} gold.")

        elif event == "A goblin ambushes you!":
            goblin = {
                "name": "Goblin",
                "health": 15,
                "damage": 3,
                "armor_class": 6,
                "dexterity": 12,
                "xp_reward": 10,
                "attacks": [
                    {"damage": 3, "type": "Slashing", "description": "The goblin slashes at you with its claws!"},
                    {"damage": 4, "type": "Piercing", "description": "The goblin stabs at you with a rusty dagger!"},
                    {"damage": 2, "type": "Bludgeoning", "description": "The goblin bashes you with a club!"}
                ]
            }
            combat(player, goblin)

        elif event == "You find a healing fountain.":
            heal_amount = random.randint(5, 15)
            player["health"] = min(player["health"] + heal_amount, player["max_health"])
            print(f"You drink from the fountain and heal {heal_amount} health. Your health is now {player['health']}.")

        elif event == "You stumble into a trap!":
            trap_damage = random.randint(5, 10)
            player["health"] -= trap_damage
            print(f"A trap is triggered! You take {trap_damage} damage. Your health is now {player['health']}.")

        elif event == "A dragonling guards the next room!":
            dragonling = {
                "name": "Dragonling",
                "health": 40,
                "damage": 10,
                "armor_class": 12,
                "dexterity": 10,
                "xp_reward": 30,
                "attacks": [
                    {"damage": 10, "type": "Slashing", "description": "The dragonling slashes at you with its claws!"},
                    {"damage": 12, "type": "Fire", "description": "The dragonling breathes fire at you!"}
                ]
            }
            combat(player, dragonling)

        elif event == "The dragon Hugh Jackman awaits you!":
            dragon = {
                "name": "Hugh Jackman",
                "health": 100,
                "damage": 20,
                "armor_class": 15,
                "dexterity": 12,
                "xp_reward": 100,
                "attacks": [
                    {"damage": 20, "type": "Fire", "description": "The dragon breathes fire at you!"},
                    {"damage": 15, "type": "Slashing", "description": "The dragon swipes at you with its claws!"},
                    {"damage": 10, "type": "Bludgeoning", "description": "The dragon slams its tail into you!"}
                ]
            }
            if combat(player, dragon):
                print("Congratulations! You have defeated the dragon Hugh Jackman and completed the dungeon!")
                print(f"Your final score is {player['score']}.")
                break

        depth += 1

# Add inventory system
if "inventory" not in player:
    player["inventory"] = []

# Function to use items from inventory
def use_item():
    if not player["inventory"]:
        print("Your inventory is empty.")
        return
    print("Your inventory:")
    for idx, item in enumerate(player["inventory"], start=1):
        print(f"{idx}. {item}")
    choice = input("Enter the number of the item you want to use (or type 'cancel' to exit): ").strip()
    if choice.lower() == "cancel":
        print("You chose not to use any item.")
        return
    try:
        item_idx = int(choice) - 1
        if 0 <= item_idx < len(player["inventory"]):
            item = player["inventory"].pop(item_idx)
            if item == "healing potion":
                heal_amount = random.randint(10, 20)
                player["health"] = min(player["health"] + heal_amount, player["max_health"])
                print(f"You used a healing potion and recovered {heal_amount} health. Current health: {player['health']}.")
            elif item == "strength potion":
                player["damage"] += 2
                print("You used a strength potion. Your damage has increased by 2 for the next battle.")
            elif item == "defense potion":
                player["defense"] += 2
                print("You used a defense potion. Your defense has increased by 2 for the next battle.")
            else:
                print(f"You used {item}, but nothing happened.")
        else:
            print("Invalid choice.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

# Expanded shop with more items
if "shop_items" not in globals():
    shop_items = {
        "healing potion": {"price": 50, "description": "Restores 10-20 HP."},
        "strength potion": {"price": 100, "description": "Increases damage by 2 for the next battle."},
        "defense potion": {"price": 100, "description": "Increases defense by 2 for the next battle."},
        "key": {"price": 75, "description": "Unlocks locked doors in the dungeon."},
        "torch": {"price": 30, "description": "Lights up dark areas in the dungeon."},
        "map": {"price": 150, "description": "Reveals hidden rooms in the dungeon."}
    }

# Updated shop function to handle inventory
def visit_shop():
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
            if player["player_gold"] >= item_price:
                update_gold_and_score(-item_price)
                player["inventory"].append(item_choice)
                print(f"You bought a {item_choice}. It has been added to your inventory.")
            else:
                print("You don't have enough gold to buy that item.")
        else:
            print("Invalid choice. Please select an item from the shop.")
        print(f"Current gold: {player['player_gold']}")  # Display player's gold after each action

# Updated dungeon exploration system
def explore_dungeon():
    """
    Handles dungeon exploration with linear progression and restrictions.
    """
    depth = 1
    while True:
        print(f"\n--- Dungeon Depth: {depth} ---")
        print("Choose your action:")
        print("1. Explore a room")
        print("2. Search for treasure")
        print("3. Fight enemies")
        print("4. Use an item")
        print("5. Return to town")
        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            explore_room()
        elif choice == "2":
            search_for_treasure()
        elif choice == "3":
            encounter_enemy(depth)
        elif choice == "4":
            use_item()
        elif choice == "5":
            print("You return to town.")
            visit_town()
            print("You travel back to the dungeon.")
        else:
            print("Invalid choice. Please select a valid option.")

        # Progress to the next depth after exploring a certain number of rooms
        depth += 1
        if depth > 10:
            print("You have reached the deepest part of the dungeon!")
            print("Prepare to face the final boss!")
            final_boss()
            break

# Final boss encounter
def final_boss():
    dragon = {
        "name": "Hugh Jackman",
        "health": 150,
        "damage": 25,
        "armor_class": 15,
        "dexterity": 12,
        "xp_reward": 200,
        "attacks": [
            {"damage": 25, "type": "Fire", "description": "The dragon breathes fire at you!"},
            {"damage": 20, "type": "Slashing", "description": "The dragon swipes at you with its claws!"},
            {"damage": 15, "type": "Bludgeoning", "description": "The dragon slams its tail into you!"}
        ]
    }
    if combat(player, dragon):
        print("Congratulations! You have defeated the dragon Hugh Jackman and completed the dungeon!")
        print(f"Your final score is {player['score']}.")
    else:
        print("You were defeated by the dragon. Game over.")

# Updated town system
def visit_town():
    print("\nYou arrive at the town. What would you like to do?")
    print("1. Visit the shop")
    print("2. Rest at the inn")
    print("3. Talk to the townsfolk")
    print("4. Return to the dungeon")
    choice = input("Enter the number of your choice: ").strip()

    if choice == "1":
        visit_shop()
    elif choice == "2":
        player["health"] = rest(player["health"], player["max_health"])
    elif choice == "3":
        print("You talk to the townsfolk and hear rumors about the dungeon.")
        print("A villager tells you about a hidden treasure deep within the dungeon.")
    elif choice == "4":
        print("You leave the town and return to the dungeon.")
    else:
        print("Invalid choice. Please select a valid option.")

# Start the game
print("Welcome to the Dungeon Explorer!")
print("In this game, you will explore a dangerous dungeon, gather treasure, and face various challenges.")
print("Your goal is to survive, gather treasure, and defeat the fearsome dragon Hugh Jackman!")
explore_dungeon()

# Fixed rest function to properly heal the player
def rest():
    """
    Allows the player to rest and recover health.
    """
    if player["health"] < player["max_health"]:
        heal_amount = random.randint(10, 20)
        player["health"] = min(player["health"] + heal_amount, player["max_health"])
        print(f"You rest and recover {heal_amount} health. Current health: {player['health']} / {player['max_health']}.")
    else:
        print("You are already at full health!")

# Updated dungeon exploration system with restricted depth progression
def explore_dungeon():
    """
    Handles dungeon exploration with linear progression and restricted depth access.
    """
    depth = 1
    rooms_explored = 0
    rooms_required_to_go_deeper = 3  # Number of rooms to explore before going deeper

    while True:
        print(f"\n--- Dungeon Depth: {depth} ---")
        print("Choose your action:")
        options = ["1. Explore a room", "2. Search for treasure", "3. Fight enemies", "4. Use an item", "5. Return to town"]
        if rooms_explored >= rooms_required_to_go_deeper:
            options.append("6. Go deeper into the dungeon")
        for option in options:
            print(option)

        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            explore_room()
            rooms_explored += 1
        elif choice == "2":
            search_for_treasure()
            rooms_explored += 1
        elif choice == "3":
            encounter_enemy(depth)
            rooms_explored += 1
        elif choice == "4":
            use_item()
        elif choice == "5":
            print("You return to town.")
            visit_town()
            print("You travel back to the dungeon.")
        elif choice == "6" and rooms_explored >= rooms_required_to_go_deeper:
            depth += 1
            rooms_explored = 0
            print(f"You venture deeper into the dungeon. You are now at depth {depth}.")
        else:
            print("Invalid choice. Please select a valid option.")

        # Check if the player has reached the final depth
        if depth > 10:
            print("You have reached the deepest part of the dungeon!")
            print("Prepare to face the final boss!")
            final_boss()
            break

# Updated town system with dynamic options
def visit_town():
    """
    Handles interactions in the town.
    """
    while True:
        print("\nYou arrive at the town. What would you like to do?")
        print("1. Visit the shop")
        print("2. Rest at the inn")
        print("3. Talk to the townsfolk")
        print("4. Return to the dungeon")
        print("5. Quit the game")
        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            visit_shop()
        elif choice == "2":
            rest()
        elif choice == "3":
            print("You talk to the townsfolk and hear rumors about the dungeon.")
            print("A villager tells you about a hidden treasure deep within the dungeon.")
        elif choice == "4":
            print("You leave the town and return to the dungeon.")
            break
        elif choice == "5":
            print(f"Thank you for playing! Your final score is {player['score']}.")
            exit()
        else:
            print("Invalid choice. Please select a valid option.")

# Updated main game loop with dynamic options
def main_game_loop():
    """
    Main game loop with dynamic options based on the player's location and progress.
    """
    while True:
        print("\nWhat would you like to do next?")
        print("1. Explore the dungeon")
        print("2. Visit the town")
        print("3. Check your inventory")
        print("4. Quit the game")
        choice = input("Enter the number of your choice: ").strip()

        if choice == "1":
            explore_dungeon()
        elif choice == "2":
            visit_town()
        elif choice == "3":
            print("Your inventory:")
            if not player["inventory"]:
                print("Your inventory is empty.")
            else:
                for idx, item in enumerate(player["inventory"], start=1):
                    print(f"{idx}. {item}")
        elif choice == "4":
            print(f"Thank you for playing! Your final score is {player['score']}.")
            break
        else:
            print("Invalid choice. Please select a valid option.")

# Start the game
print("Welcome to the Dungeon Explorer!")
print("In this game, you will explore a dangerous dungeon, gather treasure, and face various challenges.")
print("Your goal is to survive, gather treasure, and defeat the fearsome dragon Hugh Jackman!")
main_game_loop()