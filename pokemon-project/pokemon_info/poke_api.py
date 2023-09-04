import requests


def get_pokemon_info(pokemon_name):
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    response = requests.get(base_url + pokemon_name)

    if response.status_code == 200:
        pokemon_data = response.json()
        stats = pokemon_data["stats"]

        pokemon_stats = {}
        for stat in stats:
            stat_name = stat["stat"]["name"]
            base_stat = stat["base_stat"]
            pokemon_stats[stat_name] = base_stat

        return pokemon_stats
    else:
        return None
