import random


class bColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def disable(self):
        self.HEADER = ''
        self.OKBLUE = ''
        self.OKGREEN = ''
        self.WARNING = ''
        self.FAIL = ''
        self.ENDC = ''


class Person:
    def __init__(self, name, hp, mp, atk, df, magic, items):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.max_mp = mp
        self.mp = mp
        self.atk_l = atk - 10
        self.atk_h = atk + 10
        self.df = df
        self.magic = magic
        self.actions = ["Attack", "Magic", "Items"]
        self.items = items

    def generate_attack_damage(self):
        return random.randrange(self.atk_l, self.atk_h)

    # def generate_spell_damage(self, i):
    #     mgl = self.magic[i]["Damage"] - 5
    #     mgh = self.magic[i]["Damage"] + 5
    #     return random.randrange(mgl, mgh)

    def heal(self, dmg):
        self.hp += dmg
        if self.hp > self.max_hp:
            self.hp = self.max_hp

    def take_damage(self, dmg):
        self.hp -= dmg

        if self.hp < 0:
            self.hp = 0
        return self.hp

    def get_hp(self):
        return self.hp

    def get_max_hp(self):
        return self.max_hp

    def get_mp(self):
        return self.mp

    def get_max_mp(self):
        return self.max_mp

    def reduce_mp(self, cost):
        self.mp -= cost

    # def get_spell_name(self, i):
    #     return self.magic[i]["Name"]
    #
    # def get_spell_mp_cost(self, i):
    #     return self.magic[i]["Cost"]

    def choose_action(self):
        i = 1
        print(bColors.BOLD + bColors.UNDERLINE + str(self.name) + ":" + bColors.ENDC)
        print("Actions")
        for item in self.actions:
            print("\t" + str(i) + ":", item)
            i += 1

    def choose_magic(self):
        i = 1
        print("\nMagic Spells")
        for spell in self.magic:
            print("\t" + str(i) + ":", spell.name, "(cost: ", spell.cost, ")")
            i += 1

    def choose_items(self):
        i = 1
        print("\nInventory")
        for item in self.items:
            print("\t" + str(i) + ".", item["item"].name, ":", item["item"].description, ":", " ", item["quantity"],
                  "x")
            i += 1

    def choose_target_enemy(self, enemies):
        i = 1
        print("\nYour Enemies")
        for enemy in enemies:
            print("\t" + str(i) + ":"+bColors.FAIL, enemy.name, bColors.ENDC)
            i += 1
        return int(input()) - 1

    def get_enemy_stats(self):
        bar_hp = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 2
        while bar_ticks > 0:
            bar_hp += "█"
            bar_ticks -= 1
        i = len(bar_hp)
        while i < 50:
            bar_hp += " "
            i += 1
        hp_bar_fix = ""
        i = len(str(self.hp))
        while i < 5:
            hp_bar_fix += " "
            i += 1

        print("                              __________________________________________________")
        print(bColors.BOLD + self.name + "          " + hp_bar_fix + str(self.hp) + "/" + str(self.max_hp) + " |" +
              bColors.FAIL + bar_hp +
              bColors.ENDC + bColors.BOLD + "|" +
              bColors.ENDC)

    def get_stats(self):

        bar_hp = ""
        bar_ticks = (self.hp / self.max_hp) * 100 / 4
        while bar_ticks > 0:
            bar_hp += "█"
            bar_ticks -= 1
        i = len(bar_hp)
        while i < 25:
            bar_hp += " "
            i += 1

        bar_mp = ""
        bar_ticks = (self.mp / self.max_mp) * 100 / 5
        while bar_ticks > 0:
            bar_mp += "█"
            bar_ticks -= 1
        i = len(bar_mp)
        while i < 20:
            bar_mp += " "
            i += 1

        hp_bar_fix = ""
        mp_bar_fix = ""
        i = len(str(self.hp))
        while i < len(str(self.max_hp)):
            hp_bar_fix += " "
            i += 1

        i = len(str(self.mp))
        while i < len(str(self.max_mp)):
            mp_bar_fix += " "
            i += 1

        print("                             _________________________                  ____________________")
        print(bColors.BOLD + self.name + "          " + hp_bar_fix + str(self.hp) + "/" + str(self.max_hp) + " |" +
              bColors.OKGREEN + bar_hp +
              bColors.ENDC + bColors.BOLD + "|        " + mp_bar_fix + str(self.mp) + "/" + str(self.max_mp) + " |" +
              bColors.OKBLUE + bar_mp +
              bColors.ENDC + "|")
