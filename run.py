import sys
print(sys.path)

import pokemon_info
from pokemon_info import get_pokemon_attack

print(get_pokemon_attack('Ditto'))