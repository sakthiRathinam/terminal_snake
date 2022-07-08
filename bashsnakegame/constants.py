from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from typing import List,Tuple,Dict


class Directions(BaseModel):
    """directions attrs for the game"""
    left:Tuple[int,int] = (-1,0)
    right:Tuple[int,int] = (1,0)
    up:Tuple[int,int] = (0,-1)
    down:Tuple[int,int] = (0,1)
