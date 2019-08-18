import os
from pathlib import Path

folder = "World of Warcraft"

def get_game_directory():
    result = ""
    for root, dirs, files in os.walk("/"):
        if folder in dirs:
            path = Path(root)
            result = Path.home() / path / folder
            break
            
    return result