import pytest
import requests
from pokemon_info import get_pokemon_info


def test_get_pokemon_stats():
    pokemon_name = "ditto"
    stats = get_pokemon_info(pokemon_name)
    assert stats is not None, f"Failed to get stats for {pokemon_name}"


def test_pokeapi_health():
    response = requests.get("https://pokeapi.co/api/v2/")
    assert response.status_code == 200, "PokeAPI is not responding properly"

    data = response.json()
    assert "pokemon" in data, "PokeAPI response is missing 'pokemon' data"


if __name__ == "__main__":
    pytest.main()
