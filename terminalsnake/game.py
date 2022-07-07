from typing import List,Tuple,Dict
from rich import print as pp
from .colors import ColorPalette
from typing import List, Optional
from .constants import Directions
from time import sleep
from pytimedinput import timedInput
import os
class SnakeGame:
    color_palette: ColorPalette = ColorPalette()
    directions: Directions = Directions()
    def __init__(self,height:int,width:int):
        self.height: int = height
        self.width: int = width
        self.direction = self.directions.right 
        self.snake_body: List[Tuple[int,int]] = [(5,self.height//2),(4,self.height//2),(3,self.height//2)]
        self.apple_pos: Tuple[int,int] = (6,2)
        self.cells: List[Tuple[int,int]] = [(j,i) for i in range(self.height) for j in range(self.width)]
    def print_world(self):
        self.color_palette.console_print_style("terminal snake game",{"color":"magenta","blink":True,"bold":True},end=False)
        for cell in self.cells:
            if cell in self.snake_body:
                self.color_palette.console_print_style("X",{"color":"green","blink":False,"bold":True},end=True)
            elif cell[0] in (0,self.width-1) or cell[1] in  (0,self.height - 1):
                pp("[bold red]#[/bold red]" , end = "")
            elif cell == self.apple_pos:
                self.color_palette.console_print_style("$",{"color":"yellow","blink":False,"bold":True},end=True)
            else:
                pp(" ",end="")
            if cell[0] == self.width - 1:
                pp("")
    def snake(self):
        pass
    def sleepy(self,duration:Optional[float]=5) -> None:
        """ This function helps you to run tasks asynchrounsly"""
        sleep(duration)
        return None
    
    def apple(self):
        pass
    def update_game(self):
        new_head = (self.snake_body[0][0] + self.direction[0],self.snake_body[0][1] + self.direction[1])
        self.snake_body.insert(0,new_head)
        self.snake_body.pop(-1)
    def start_game(self):
        while True:
            #clear screen
            print("\x1b[2J\x1b[1;13H")
            # print("\073[H")

            #print field drawing
            self.print_world()
            #sleep and get input
            txt,_ = timedInput('get input',timeout=0.4)
            #update the game
            self.update_game()
