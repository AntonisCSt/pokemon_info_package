from pokemon_info.poke_api import get_pokemon_info


def main():
    pokemon_name = input("Enter a Pokemon's name: ")
    pokemon_stats = get_pokemon_info(pokemon_name.lower())

    if pokemon_stats:
        print("Pokemon Stats:")
        print(pokemon_stats)
    else:
        print("Pokemon not found or an error occurred.")


if __name__ == "__main__":
    main()
