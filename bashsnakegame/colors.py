from typing import Dict, List, Optional

from pydantic import BaseModel
from rich.console import Console
from rich.style import Style


class ColorPalette:
    console: Console = Console()

    def __init__(self):
        pass

    def get_style(self, color_config: Dict[str, any]) -> Style:
        return Style(**color_config)

    def console_print_style(
        self, message: str, color_config: Dict[str, any], end: bool
    ) -> any:
        self.console.print(
            message, style=self.get_style(color_config)
        ) if not end else self.console.print(
            message, style=self.get_style(color_config), end=""
        )
