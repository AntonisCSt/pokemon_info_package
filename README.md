# Pokemon info package

This repo is a part of the #project-of-the-week channel of DataTalksClub

# What is this package about

This package provides information about Pokemon. You add the name of the Pokemon and the package provides the information. It is based on the Pokemon API: `https://pokeapi.co/api/v2/pokemon/`

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

# Test the code and checkout linting/formatting

`make test`

`make quality_check`

# Other useful information about the project

Building package using __main__.py approach

What is the purpose of `python -m`?
Answer taken by reddit post : `https://www.reddit.com/r/learnpython/comments/r1owm7/what_is_the_m_flags_purpose/`


When you run a script directly like python path/to/myscript.py the name of that module in the process will not be path.to.myscript, instead the name will be implicitly forced to __main__. That’s why you add the if __name__ == '__main__': (aka the main guard) to scripts so that the portion under there only gets run if it was the module executed along with the python command.

Installed modules can have that main guard too, but how would you call those scripts/modules from the command line? You’d need to know the path to where they are which is usually some convoluted location on your computer. Instead, you can use python -m some.module. Python will find the appropriate module that matches that module path and execute it as the main module, changing its __name__ to '__main__'.

Another less-known thing that the -m flag does, is that it prevents the directory holding the executed script from being added to the PYTHONPATH. Let’s go back to our original example, when you do this: python path/to/myscript.py. Python adds path/to to the front of your PYTHONPATH. So for example if you had a file in there called path/to/threading.py then anytime in your program you do import threading, it will grab the one from this directory instead of the installed threading library, which is not desirable. If you instead did python -m path.to.myscript then this PYTHONPATH prepending doesn’t happen and you can safely ignore potentially conflicting package/module names.
