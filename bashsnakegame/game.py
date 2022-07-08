import os
import random
from time import sleep
from typing import Dict, List, Optional, Tuple

from pytimedinput import timedInput
from rich import print as pp

from .colors import ColorPalette
from .constants import Directions
from .terminal_arts import *


class SnakeGame:
    color_palette: ColorPalette = ColorPalette()
    directions: Directions = Directions()

    def __init__(self, height: int, width: int):
        self.height: int = height
        self.width: int = width
        self.score: int = 0
        self.direction = self.directions.right
        self.snake_body: List[Tuple[int, int]] = [
            (5, self.height // 2),
            (4, self.height // 2),
            (3, self.height // 2),
        ]  # initalizing the snake body
        self.apple_pos: Tuple[int, int] = (6, 2)  # apple position in intial state
        self.cells: List[Tuple[int, int]] = [
            (j, i) for i in range(self.height) for j in range(self.width)
        ]

    def print_world(self) -> None:
        """
        this func print the terminal world,snake,apple everything in the game using
        color_palette from rich
        :no params
        :no return
        """
        self.color_palette.console_print_style(
            snake_logo, {"color": "magenta", "blink": True, "bold": True}, end=False
        )
        self.color_palette.console_print_style(
            help_text, {"color": "blue", "blink": False, "bold": True}, end=False
        )
        self.color_palette.console_print_style(
            f"your score {self.score} to win the game need to reach score of {(self.height -2) * (self.width - 2)}",
            {"color": "blue", "blink": False, "bold": True},
            end=False,
        )
        for cell in self.cells:
            if cell in self.snake_body:
                self.color_palette.console_print_style(
                    "X", {"color": "green", "blink": False, "bold": True}, end=True
                )
            elif cell[0] in (0, self.width - 1) or cell[1] in (0, self.height - 1):
                pp("[bold red]#[/bold red]", end="")
            elif cell == self.apple_pos:
                self.color_palette.console_print_style(
                    "$", {"color": "yellow", "blink": False, "bold": True}, end=True
                )
            else:
                pp(" ", end="")
            if cell[0] == self.width - 1:
                pp("")

    def sleepy(self, duration: Optional[float] = 5) -> None:
        """This func helps you to run tasks asynchrounsly
        :duration:float optional
        :no return
        """
        sleep(duration)
        return None

    def change_apple_position(self) -> None:
        """this func change the apple to valid position if apple is eaten by snake :no params
        :no return
        """
        new_pos = (
            random.choice([i for i in range(1, self.width - 2)]),
            random.choice([i for i in range(1, self.height - 2)]),
        )
        while new_pos in self.snake_body:
            new_pos = (
                random.choice([i for i in range(1, self.width - 2)]),
                random.choice([i for i in range(1, self.height - 2)]),
            )
        self.apple_pos = new_pos

    def got_apple(self) -> None:
        """this func increase the current score and call the change_apple_postion to chagne the apple pos and print the world to reflect the changes
        :no params
        :no return
        """
        if self.apple_pos == self.snake_body[0]:
            self.snake_body.insert(0, self.apple_pos)
            self.score += 1
            self.change_apple_position()
            self.print_world()

    def check_win(self) -> None:
        """this func check the score and determine you have completed all boxes then return the win screen to terminal
        :no params
        :no return
        """
        if self.score >= (self.height - 2) * (self.width - 2):
            print("\x1b[2J\x1b[1;13H")
            self.color_palette.console_print_style(
                win_screen, {"color": "blue", "blink": False, "bold": True}, end=False
            )
            return True
        return False

    def update_game(self):
        """this func will change the snake head to directions you have commanded and move accordingly the previous direction if nothing commanded as a input
        :no params
        :no return
        """
        new_head = (
            self.snake_body[0][0] + self.direction[0],
            self.snake_body[0][1] + self.direction[1],
        )
        self.snake_body.insert(0, new_head)
        self.snake_body.pop(-1)

    def print_death_screen(self):
        """this func will change the snake head to directions you have commanded and move accordingly the previous direction if nothing commanded as a input
        :no params
        :no return
        """
        # clear screen
        print("\x1b[2J\x1b[1;13H")
        self.color_palette.console_print_style(
            death_screen, {"color": "red", "blink": True, "bold": True}, end=True
        )

    def start_game(self):
        """this func will start the game and get the timed input for 0.4 seconds and continue till the while loop breaks
        :no params
        :no return
        """
        while True:
            # clear screen
            print("\x1b[2J\x1b[1;13H")
            # print("\073[H")
            # print field drawing
            self.print_world()
            # sleep and get input
            txt, _ = timedInput("get input", timeout=0.4)
            # update the game
            match txt:
                case "w" | "W":
                    self.direction = self.directions.up
                case "s" | "S":
                    self.direction = self.directions.down
                case "a" | "A":
                    self.direction = self.directions.left
                case "d" | "D":
                    self.direction = self.directions.right
                case "q" | "quit" | "Q":
                    break
            # update the game
            self.got_apple()
            self.update_game()

            # check died
            if self.snake_body[0][0] in [0, self.width - 1] or self.snake_body[0][
                1
            ] in [0, self.height - 1]:
                self.print_death_screen()
                break
            # check win
            if self.check_win():
                break
