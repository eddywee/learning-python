from classes.game import Person, bcolors

magic = [{"Name": "Fire", "Cost": "10", "Damage": 60},
        {"Name": "Frost", "Cost": "10", "Damage": 60},
        {"Name": "Arcane", "Cost": "10", "Damage": 60}]

player  = Person("vame",460, 65, 60, 34, magic, None)

print(player.generate_damage())
print(player.generate_damage())
print(player.generate_damage())

print(player.generate_spell_damage(1))