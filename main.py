"""
Blueface November 2023 - Hackathon Arcade Game

"Calls of Duty"

Bluethesda Team
---------------
James Spencer
Ivan Chulkov
Niall Caffrey
Yash Palwe
Declan Cox

"""
import os

import arcade
from dotenv import load_dotenv

from arcade_game.arcade_platformer.config.config import SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE
from arcade_game.arcade_platformer.player.player import Player
from arcade_game.arcade_platformer.view.welcome_view import WelcomeView
from arcade_game.arcade_platformer.view.media_player import MediaPlayer
from log.config_log import logger

if __name__ == "__main__":

    logger.info("Game started")

    # Load environment variables
    load_dotenv()

    # 1st let's check the speech venv variables were properly set, if not let's throw an error with instructions
    if not os.environ.get('SPEECH_API_KEY') and not os.environ.get('SPEECH_REGION'):
        raise Exception("You need to set the speech key and speech region. Read readme file for instructions.")

    window = arcade.Window(
        width=SCREEN_WIDTH, height=SCREEN_HEIGHT, title=SCREEN_TITLE
    )

    global_player: Player = Player()

    intro_player = MediaPlayer("2050-Neon-Skies.wav")

    welcome_view = WelcomeView(global_player, intro_player)
    window.show_view(welcome_view)

    arcade.run()

    # Closes the speech processor
    if welcome_view:
        welcome_view.cleanup()

    logger.info("Game over")
