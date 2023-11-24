from multiprocessing import Process, Queue
import time
import arcade
import os
from arcade_game.arcade_platformer.config.config import SCREEN_WIDTH, SCREEN_HEIGHT, ASSETS_PATH
from . import start_view
from arcade_game.arcade_platformer.player.player import Player

class WelcomeView(arcade.View):
    """
    Displays a welcome screen and prompts the user to begin the game.

    Displays a background image, play a sounds and wait for pressing the Enter key to start the game.
    You do not have to modify these to complete the mandatory challenges.
    """

    def __init__(self, player: Player) -> None:
        super().__init__()

        self.player = player

        self.game_view = None
        self.intro_sound = None
        self.sound_player = None

        # Find the title image in the images folder
        first_image_path = ASSETS_PATH / "images" / "all_is_calm.png"

        # Load our title image
        self.first_image = arcade.load_texture(first_image_path)

        # Set our display timer
        self.display_timer = 2.0
        # Set our display timer
        self.switch_screen_timer = 0.0

        # Are we showing the instructions?
        self.show_instructions = False


    def on_update(self, delta_time: float) -> None:
        """Manages the timer to toggle the instructions

        Arguments:
            delta_time -- time passed since last update
        """
        
        # First, count down the time
        self.display_timer -= delta_time
        self.switch_screen_timer += delta_time
        
        # If the timer has run out, we toggle the instructions
        if self.display_timer < 0:
            # Toggle whether to show the instructions
            self.show_instructions = not self.show_instructions

            # And reset the timer so the instructions flash slowly
            self.display_timer = 1.0

        # If the timer has run out, we toggle the instructions
        if self.switch_screen_timer > 1:
            self.start_view = start_view.StartView(self.player)
            self.window.show_view(self.start_view)

    def on_draw(self) -> None:
        # Start the rendering loop
        arcade.start_render()

        # Draw a rectangle filled with our title image
        arcade.draw_texture_rectangle(
            center_x=SCREEN_WIDTH / 2,
            center_y=SCREEN_HEIGHT / 2,
            width=SCREEN_WIDTH,
            height=SCREEN_HEIGHT,
            texture=self.first_image,
        )

    def start_sound(self) -> None:
        # Load & play intro music
        self.intro_sound = arcade.load_sound(
            str(ASSETS_PATH / "sounds" / "2050-Neon-Skies.wav")
        )
        self.sound_player = self.intro_sound.play(volume=0.3, loop=True)

    def stop_sound(self) -> None:
        """Stops the intro music"""
        if self.intro_sound != None:
            self.intro_sound.stop(self.sound_player)
