import sys

print(sys.path)

import pokemon_info
from pokemon_info import get_pokemon_info,get_pokemon_attack, get_pokemon_defense

print(get_pokemon_info('charmander'))
print(get_pokemon_attack('Ditto'))
print(get_pokemon_defense('Ditto'))
