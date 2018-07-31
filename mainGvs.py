import random

from classes.rpgGame import Person, bColors
from classes.magic import Spell
from classes.inventory import Item

# black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

# create items
potion = Item("Potion", "potion", "Heals 50 HP", 50)
hi_potion = Item("Hi-Potion", "potion", "Heals 100 HP", 100)
super_potion = Item("Super Potion", "potion", "Heals 500 HP", 500)
elixer = Item("Elixer", "elixer", "Fully restores HP/MP of one party member", 9999)
hi_elixer = Item("MegaElixer", "elixer", "Fully restores party's HP/MP", 9999)

grenade = Item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, cure, cura]
player_items = [{"item": potion, "quantity": 10}, {"item": hi_potion, "quantity": 5},
                {"item": super_potion, "quantity": 4}, {"item": elixer, "quantity": 3},
                {"item": hi_elixer, "quantity": 2}, {"item": grenade, "quantity": 1}]
# instantiate people
player1 = Person("cool_kid", 1000, 150, 30, 20, player_spells, player_items)
player2 = Person("lucifer ", 1500, 120, 80, 50, player_spells, player_items)
player3 = Person("kisuke  ", 1200, 100, 100, 40, player_spells, player_items)

enemy1 = Person("Lancelot", 1000, 60, 400, 25, [], [])
enemy2 = Person("Johnson", 12000, 60, 200, 60, [], [])
enemy3 = Person("Odette  ", 1000, 160, 400, 20, [], [])

players = [player1, player2, player3]
enemies = [enemy1, enemy2, enemy3]
running = True
i = 0

print(bColors.FAIL + bColors.BOLD + "An Enemy Attacks!" + bColors.ENDC)

while running:
    print("\n\n")
    print("NAME                         HP                                         MP")
    for player in players:
        player.get_stats()
    print("\n")
    for enemy in enemies:
        enemy.get_enemy_stats()
    print("\n")

    for player in players:
        print("=============================")
        player.choose_action()
        choice = input("Choose Action(What'll You Do Now?):")
        index = int(choice) - 1

        if index == 0:
            dmg = player.generate_attack_damage()
            target_enemy = player.choose_target_enemy(enemies)
            enemies[target_enemy].take_damage(dmg)
            print(player.name + " attacked for ", dmg, " points of damage.To " + enemies[target_enemy].name + "\n")
            if enemies[target_enemy].get_hp() == 0:
                print(enemies[target_enemy].name + " have been slan! By " + player.name)
                del enemies[target_enemy]

        elif index == 1:
            player.choose_magic()
            magic_choice = int(input("Choose Magic: ")) - 1

            if magic_choice == -1:
                continue
            spell = player.magic[magic_choice]
            magic_dmg = spell.generate_damage()

            current_mp = player.get_mp()

            if current_mp < spell.cost:
                print(bColors.FAIL + "Not Enough Mana" + bColors.ENDC)
                continue
            player.reduce_mp(spell.cost)

            if spell.type == "white":
                player.heal(magic_dmg)
                print(bColors.OKBLUE + "\n" + spell.name + " Heals for ", magic_dmg,
                      " points of health." + bColors.ENDC)
            elif spell.type == "black":
                # enemy.take_damage(magic_dmg)
                target_enemy = player.choose_target_enemy(enemies)
                enemies[target_enemy].take_damage(magic_dmg)

                print(bColors.OKBLUE + "\n" + spell.name + " deals ", magic_dmg, " points of damage. To "
                      + enemies[target_enemy].name
                      + bColors.ENDC)
                if enemies[target_enemy].get_hp() == 0:
                    print(enemies[target_enemy].name + " have been slan! By " + player.name)
                    del enemies[target_enemy]
        elif index == 2:
            player.choose_items()
            item_choice = int(input("Choose item: ")) - 1

            if item_choice == -1:
                continue
            if player_items[item_choice]["quantity"] == 0:
                print(bColors.FAIL + "None Left..." + bColors.ENDC)
                continue

            item = player_items[item_choice]["item"]
            player_items[item_choice]["quantity"] -= 1

            if item.type == "potion":
                player.heal(item.prop)
                print(bColors.OKGREEN, item.name, " : ", item.description, bColors.ENDC)

            elif item.type == "elixer":
                if item.name == "MegaElixer":
                    for i in players:
                        i.hp = i.max_hp
                        i.mp = i.max_mp
                else:
                    player.hp = player.max_hp
                    player.mp = player.max_mp
                print(bColors.OKGREEN, item.name, " : ", item.description, bColors.ENDC)

            elif item.type == "attack":
                # enemy.take_damage(item.prop)
                target_enemy = player.choose_target_enemy(enemies)
                enemies[target_enemy].take_damage(item.prop)
                print(bColors.FAIL, item.name, " : ", item.description, " To " + enemies[target_enemy].name,
                      bColors.ENDC)
                if enemies[target_enemy].get_hp() == 0:
                    print(enemies[target_enemy].name + " have been slan! By " + player.name)
                    del enemies[target_enemy]

    enemy_choice = 1

    for enemy in enemies:
        enemy_dmg = enemy.generate_attack_damage()
        victim = random.randrange(0, 3)
        players[victim].take_damage(enemy_dmg)
        print(enemy.name + " Attacks for ", enemy_dmg, " points of damage. To " + players[victim].name + "\n")

        if players[victim].get_hp() == 0:
            print(enemies[victim].name + " have been slan! By " + enemy.name)
            del players[victim]

    print("---------------------------------")

    enemy_dead = 0
    player_dead = 0
    for enemy in enemies:
        if enemy.get_hp() == 0:
            enemy_dead += 1
    for player in players:
        if player.get_hp() == 0:
            player_dead += 1

    if enemy_dead == 3:
        print(bColors.OKGREEN + "You Win!\nCongratulations." + bColors.ENDC)
        running = False
    elif player_dead == 3:
        print(bColors.FAIL + "You Team have been Defeated!" + bColors.ENDC)
        running = False
