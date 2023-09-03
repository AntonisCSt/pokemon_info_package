# Inside poke_functions.py
from pokemon_info.poke_api import get_pokemon_info

def get_pokemon_attack(pokemon_name):
    pokemon_stats = get_pokemon_info(pokemon_name.lower())
    return pokemon_stats['attack']
