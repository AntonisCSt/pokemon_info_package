# Pokemon info package

This repo is a part of the #project-of-the-week channel of DataTalksClub

# What is this package about

This package provides information about Pokemon. You add the name of the Pokemon and the package provides the information. It is based on the pokemon API: `https://pokeapi.co/api/v2/pokemon/`

# How to use it?

```python
import pokemon_info
from pokemon_info import get_pokemon_info,get_pokemon_attack, get_pokemon_defense

print(get_pokemon_info('charmander'))
print(get_pokemon_attack('Ditto'))
print(get_pokemon_defense('Ditto'))
##Output:
# {'hp': 39, 'attack': 52, 'defense': 43, 'special-attack': 60, 'special-defense': 50, 'speed': 65}
# 48
# 48
```


# How to install it locally

cd into pokemon-project and activate the venv of your choice.

```t
local install editable command:
`python -m pip install -e .`
Where `-m` stands for module and `-e` stands for editable.
```

# Test the code and checkout linting/formating

`make test`

`make quality_check`

# Other useful information about the project

Building package using __main__.py approach

