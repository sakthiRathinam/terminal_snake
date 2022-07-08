# terminal_snake

[![image](https://img.shields.io/pypi/v/bashsnakegame.svg?style=flat)](https://pypi.python.org/pypi/tortoise-cli)
[![image](https://img.shields.io/github/license/sakthiRathinam/terminal_snake
)](https://github.com/sakthiRathinam/terminal_snake)
[![image](https://github.com/sakthiRathinam/terminal_snake/workflows/pypi/badge.svg)](https://github.com/sakthiRathinam/terminal_snake/actions?query=workflow:pypi)

A cli for snake game in python using graph algo and vanilla python without using no gui libraries nothing only logic and python.

## Installation

You can just install from pypi.

```shell
pip install bashsnakegame
```

## Quick Start

```                                                   
create a python file and paste this                                                                                                              
from bashsnakegame.game import SnakeGame

def main():
    #width will be the first arg and height will be the second arg based on that i will draw the cells in the terminal
    game = SnakeGame(10,20)
    game.start_game()
main()

Commands:
  shell  run the python file and your game starts.
  
```

## License

This project is licensed under the
[MIT](https://github.com/tortoise/tortoise-cli/blob/main/LICENSE) License.